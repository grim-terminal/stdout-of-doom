"""Command line entry point: python -m doom.cli app.log"""
import argparse
import sys

from doom import cache
from doom.filtering import compile_filter
from doom.parse import parse_lines
from doom.report import render, summarize


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="doom", description="Summarise a log file")
    parser.add_argument("logfile", help="path to the log file, or - for stdin")
    parser.add_argument("--filter", help="expression over level, message and time, e.g. \"level == 'ERROR'\"")
    parser.add_argument("--cache", help="file to keep the parsed entries in")
    return parser


def main(argv=None) -> int:
    args = build_parser().parse_args(argv)
    entries = cache.load(args.cache) if args.cache else None
    if entries is None:
        if args.logfile == "-":
            entries = list(parse_lines(sys.stdin))
        else:
            with open(args.logfile, encoding="utf-8") as f:
                entries = list(parse_lines(f))
        if args.cache:
            cache.save(args.cache, entries)
    if args.filter:
        entries = [e for e in entries if compile_filter(args.filter)(e)]
    levels, errors = summarize(entries)
    print(render(levels, errors))
    return 0


if __name__ == "__main__":
    sys.exit(main())
