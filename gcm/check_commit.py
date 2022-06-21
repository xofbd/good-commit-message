#!/usr/bin/env python3
import re
import sys

LENGTH_HEADER = 50
LENGTH_BODY = 72


def load_lines(f):
    """Return list of lines of commit message

    The newline character at the end of the line should be removed as it
    should not count towards the character limit.
    """
    return [re.sub(r"\n$", "", line) if line != "\n" else line for line in f]


def validate_header(header):
    """Return dictionary with validation results of header

    1. The header cannot begin with a lowercase character
    2. The number of characters cannot exceed the header length limit
    3. The header cannot end in a period mark
    """
    return {
        "header_capitalization": not header[0].islower(),
        "header_length": len(header) <= LENGTH_HEADER,
        "header_punctuation": header[-1] != ".",
    }


def validate_body(body):
    """Return dictionary of validation results of body

    1. If the commit message has a body, then a blank line separates the header
       with the rest of the commit message (the body)
    2. Each line of the body cannot exceed the body character length limit
    """
    if not body:
        return {
            "blank_line": True,
            "body_lines_length": True,
        }

    return {
        "blank_line": body[0] == "\n",
        "body_lines_length": all([len(line) <= LENGTH_BODY for line in body[1:]]),
    }


def validate_list(body, marker=None):
    """Return dictionary of validation results of lists in body

    1. lists begin with '* ' or '- '
    2. list items need a space after the marker
    3. lists terminate with a blank line
    """
    if not body:
        return {"body_list": True}

    # We have found the beginning of a list
    if marker is None and (body[0].startswith("* ") or body[0].startswith("- ")):
        return validate_list(body[1:], marker=body[0][0])

    # Continue finding a list in the body
    if marker is None:
        return validate_list(body[1:])

    # Lists terminate with a new line
    if body[0].startswith(f"{marker} ") or body[0].startswith("  "):
        return validate_list(body[1:], marker=marker)
    elif body[0] == "\n":
        return validate_list(body[1:])
    else:
        return {"body_list": False}


def alert_errors(test_results):
    """Send messages of reason for failure to stdout"""
    error_messages = {
        "header_capitalization": "* Header should use sentence capitalization",
        "header_length": f"* Header exceeds {LENGTH_HEADER} characters",
        "header_punctuation": "* Header ends with a .",
        "blank_line": "* There is no blank line separating header with commit body",
        "body_lines_length": f"* Body lines exceed {LENGTH_BODY} characters",
        "body_list": "* Lists in commit body are not formatted properly",
    }

    if all(test_results.values()):
        return

    print("Commit message was rejected because:\n", file=sys.stderr)

    for test, result in test_results.items():
        if not result:
            print(error_messages[test], file=sys.stderr)

    print("\nTo skip the check, run:\n     git commit --no-verify", file=sys.stderr)
    print("To recover your previous commit message, run:", file=sys.stderr)
    print(
        "    "
        "git commit -e --file=$(git rev-parse --git-dir)/COMMIT_EDITMSG",
        file=sys.stderr
    )


def main(f):
    lines = load_lines(f)
    test_results = {}

    test_results.update(validate_header(lines[0]))
    test_results.update(validate_body(lines[1:]))
    test_results.update(validate_list(lines[1:]))

    if not all(test_results.values()):
        alert_errors(test_results)
        sys.exit(1)
    else:
        sys.exit(0)


if __name__ == "__main__":
    from argparse import ArgumentParser, FileType

    parser = ArgumentParser(
        description="Check that commit message follows the standard"
    )
    parser.add_argument(
        "path",
        type=FileType("r"),
        help="path to commit message file, defaults to stdin",
        nargs="?",
        default=sys.stdin
    )
    args = parser.parse_args()

    main(args.path)
