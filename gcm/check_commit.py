#!/usr/bin/env python3
import sys

LENGTH_HEADER = 50
LENGTH_BODY = 72


def load_lines(f):
    """Return list of lines of commit message"""
    return f.readlines()


def validate_header(header):
    """Return True if header fits the standard"""
    if header[0].islower():
        return False

    if len(header) > LENGTH_HEADER:
        return False

    if header[-1] == ".":
        return False

    return True


def validate_body(body):
    """Return True if the lines of the body fit the standard"""
    # The case of no body text
    if not body:
        return True

    # If the commit message contained a body, then there should be a blank line
    # separating the header with the rest of the body
    if body[0] != "\n":
        return False

    # All lines of the body must be within the length limit
    for line in body[1:]:
        if len(line) > LENGTH_BODY:
            return False

    # Validate all lists in the body
    return validate_list(body)


def validate_list(body, marker=None):
    """Return True if a body with a list follows the standard"""
    if marker is None:
        marker = body[0][0]

    if not body or body[0] == "\n":
        return True

    if body[0].startswith(f"{marker} ") or body[0].startswith("  "):
        return validate_list(body[1:], marker)
    else:
        return False


def main(f):
    lines = load_lines(f)
    valid_header = validate_header(lines[0])
    valid_body = validate_body(lines[1:])

    if valid_body and valid_header:
        sys.exit(0)
    else:
        print("Commit message did not meet the convention", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    from argparse import ArgumentParser, FileType

    parser = ArgumentParser(description="Check that commit message follows convention")
    parser.add_argument(
        "path",
        type=FileType("r"),
        help="path to commit message file, defaults to stdin",
        nargs="?",
        default=sys.stdin
    )
    args = parser.parse_args()

    main(args.path)
