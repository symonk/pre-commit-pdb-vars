import argparse
import ast
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


def check_vars(filenames: str):
    """
    For each of the file paths passed to the hook; parse the AST for the given file
    and find all variable names, then match them against the predefined `shortcuts`
    of pdb commands.  If any variable is in violation, exit 1 else exit 0.
    :param filenames: Sequence of files passed to the hook
    :return: The exit code.
    """
    for file in filenames:
        with open(file) as f:
            root = ast.parse(f.read())
            names = [
                name
                for name in sorted(
                    {
                        node.id
                        for node in ast.walk(root)
                        if isinstance(node, ast.Name)
                        and not isinstance(node.ctx, ast.Load)
                    }
                )
                if matches(name)
            ]
            for name in names:
                print(f"Variable named: `{name}` mirrors a pdb command, rename it.")
                return 1
    return 0


def matches(variable_name: str) -> bool:
    """
    Check if the parsed variable name is an offender, if an offender is found
    exit code `1` will be returned downstream.
    :param variable_name: The parsed python file variable name
    :return: Boolean indicating if the variable name is prohibited.
    """
    return variable_name in PDB_SHORTCUTS


if __name__ == "__main__":
    raise SystemExit(main())
