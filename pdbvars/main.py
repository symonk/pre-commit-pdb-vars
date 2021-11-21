import argparse
import ast
import dataclasses
import os
import typing

PDB_SHORTCUTS = (
    "h",
    "w",
    "d",
    "u",
    "b",
    "tbreak",
    "cl",
    "disable",
    "enable",
    "ignore",
    "condition",
    "commands",
    "s",
    "n",
    "unt",
    "r",
    "c",
    "j",
    "l",
    "ll",
    "a",
    "p",
    "pp",
    "whatis",
    "source",
    "display",
    "undisplay",
    "interact",
    "alias",
    "unalias",
    "run",
    "restart",
    "q",
    "debug",
    "retval",
)


def main(argv: typing.Optional[typing.Sequence[str]] = None) -> int:
    """
    Core entry point to the hook.
    :param argv: Command line args
    :return: The exit code (int)
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("filenames", nargs="*")
    args = parser.parse_args(argv)
    return check_vars(args.filenames)


class PdbParser(ast.NodeVisitor):
    """
    Captures `violations` of pdb command variable naming.  At present we check that
    standard assignments and function names do not mirror that of a pdb command shortcut.

        :: Supports
            :: Function Def
            :: Name
            :: More coming in future.
    """

    def __init__(self) -> None:
        self.violations: typing.List[Violation] = []
        self.current_file = ""  # Todo: Terrible concept; refactor.

    def visit_Name(self, node: ast.Name) -> typing.Any:
        if node.id in PDB_SHORTCUTS:
            self.violations.append(
                Violation(
                    self.current_file, "name", node.lineno, node.col_offset, node.id
                )
            )

    def visit_FunctionDef(self, node: ast.FunctionDef) -> typing.Any:
        if node.name in PDB_SHORTCUTS:
            self.violations.append(
                Violation(
                    self.current_file,
                    "function def",
                    node.lineno,
                    node.col_offset,
                    node.name,
                )
            )


@dataclasses.dataclass(frozen=True)
class Violation:
    mod: str
    node_type: str
    line_no: int
    column: int
    shortcut: str

    def __repr__(self) -> str:
        return (
            f"Prohibited PDB Command {self.node_type} "
            f"`{self.shortcut}` at: "
            f"{os.path.abspath(self.mod)}:{self.line_no}:{self.column}."
        )


def _walk_nodes(filepath: str, visitor: ast.NodeVisitor):
    with open(filepath) as f:
        visitor.visit(ast.parse(f.read(), filename=filepath))


def check_vars(filenames: str):
    """
    For each of the file paths passed to the hook; parse the AST for the given file
    and find all variable names, then match them against the predefined `shortcuts`
    of pdb commands.  If any variable is in violation, exit 1 else exit 0.

    :param filenames: Sequence of files passed to the hook
    :return: The exit code.
    """
    visitor = PdbParser()
    for file in filenames:
        visitor.current_file = file
        _walk_nodes(file, visitor)
        if visitor.violations:
            for violation in visitor.violations:
                print(violation)
            return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
