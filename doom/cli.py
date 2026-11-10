"""Command line entry point: python -m doom.cli app.log"""
import argparse
import sys

from doom.parse import parse_lines
from doom.since import parse_age, recent
from doom.report import render, summarize


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="doom", description="Summarise a log file")
    parser.add_argument("logfile", help="path to the log file, or - for stdin")
    parser.add_argument("--since", help="only entries from the last N minutes, hours or days, e.g. 15m, 2h, 1d")
    return parser


def main(argv=None) -> int:
    args = build_parser().parse_args(argv)
    if args.logfile == "-":
        entries = list(parse_lines(sys.stdin))
    else:
        with open(args.logfile, encoding="utf-8") as f:
            entries = list(parse_lines(f))
    if args.since:
        entries = recent(entries, parse_age(args.since))
    levels, errors = summarize(entries)
    print(render(levels, errors))
    return 0


if __name__ == "__main__":
    sys.exit(main())
