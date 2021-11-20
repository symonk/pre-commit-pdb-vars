import argparse
import typing

shortcuts = (
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
    parser = argparse.ArgumentParser()
    parser.add_argument("filenames", nargs="*")
    args = parser.parse_args(argv)
    return check_vars(args.filenames)


def check_vars(filenames):
    for file in filenames:
        print(file)
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
