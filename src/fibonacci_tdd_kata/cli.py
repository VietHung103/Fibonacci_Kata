import argparse

from fibonacci_tdd_kata.core import fibonacci


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="fibonacci-tdd-kata",
        description="Print the Fibonacci value for one number, or a range of numbers.",
    )
    parser.add_argument(
        "n",
        type=int,
        nargs="?",
        help="A single number to convert (ignored if --start/--end are given).",
    )
    parser.add_argument("--start", type=int, help="Start of the range (inclusive).")
    parser.add_argument("--end", type=int, help="End of the range (inclusive).")
    return parser


def main() -> None:
    parser = build_parser()
    args = parser.parse_args()
    if args.start is not None and args.end is not None:
        for i in range(args.start, args.end + 1):
            print(fibonacci(i))
    elif args.n is not None:
        print(fibonacci(args.n))
    else:
        parser.error("Provide either a single number, or --start and --end.")


if __name__ == "__main__":
    main()
