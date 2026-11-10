"""Command line entry point: python -m doom.cli app.log"""
import argparse
import sys

from doom.parse import parse_lines
from doom.publish import post_summary
from doom.report import render, summarize


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="doom", description="Summarise a log file")
    parser.add_argument("logfile", help="path to the log file, or - for stdin")
    parser.add_argument("--report-to", action="store_true", help="also send the summary to the central collector")
    return parser


def main(argv=None) -> int:
    args = build_parser().parse_args(argv)
    if args.logfile == "-":
        levels, errors = summarize(parse_lines(sys.stdin))
    else:
        with open(args.logfile, encoding="utf-8") as f:
            levels, errors = summarize(parse_lines(f))
    print(render(levels, errors))
    if args.report_to:
        post_summary(levels, errors)
    return 0


if __name__ == "__main__":
    sys.exit(main())
