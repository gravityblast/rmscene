"""Experimental cli helpers."""

import sys
import argparse
from . import read_blocks, SceneGlyphItemBlock
import logging
from logger import _logger
import json


def parse_args(args):
    parser = argparse.ArgumentParser(prog="rmscene")
    parser.add_argument("file", type=argparse.FileType("rb"), help="filename to read")
    parser.add_argument("-v", action="store_true")
    return parser.parse_args(args)


def pprint_file(args) -> None:
    if args.v:
        _logger.setLevel(logging.DEBUG)

    result = read_blocks(args.file)
    lines = []
    for el in result:
        if el.__class__ == SceneGlyphItemBlock:
            lines.append(el.item.value.text)

    print(json.dumps(lines))

def main():
    args = parse_args(sys.argv[1:])
    pprint_file(args)
