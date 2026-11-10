"""Command line entry point: python -m doom.cli app.log"""
import argparse
import sys

from doom.grep import grep
from doom.parse import parse_lines
from doom.report import render, summarize


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="doom", description="Summarise a log file")
    parser.add_argument("logfile", help="path to the log file, or - for stdin")
    parser.add_argument("--grep", help="only entries whose message matches this regular expression")
    return parser


def main(argv=None) -> int:
    args = build_parser().parse_args(argv)
    if args.logfile == "-":
        lines = sys.stdin.read().splitlines()
    else:
        lines = open(args.logfile, encoding="utf-8").read().splitlines()
    entries = list(parse_lines(lines))
    if args.grep:
        try:
            entries = grep(entries, args.grep)
        except:
            print("bad pattern", file=sys.stderr)
            return 2
    levels, errors = summarize(entries)
    print(render(levels, errors))
    return 0


if __name__ == "__main__":
    sys.exit(main())
