import argparse
import typing


def main(argv: typing.Optional[typing.Sequence[str]] = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("filenames", nargs="*")
    args = parser.parse_args(argv)
    return check_vars(args.filenames)


def check_vars(filenames):
    print(filenames)
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
