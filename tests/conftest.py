from pathlib import Path

import pytest


@pytest.fixture
def path_good():
    return Path("tests") / "data" / "COMMIT_MSG_GOOD"


@pytest.fixture
def path_bad():
    return Path("tests") / "data" / "COMMIT_MSG_BAD"


@pytest.fixture
def message_lines_good():
    return [
        "A good commit message header",
        "\n",
        "There is a blank line between the header and rest of the body. We also",
        "make sure we don't go beyond the 72 character limit.",
        "\n",
        "- We can also support lists",
        "- just make sure we have a space between",
        "- either a hyphen or asterisk",
        "\n",
        "Here's another paragraph. We can also have more than one.",
        "\n",
        "* asterisks are allowed",
        "* for lists",
    ]


@pytest.fixture
def message_lines_no_blank():
    return [
        "A good commit message header",
        "There is a blank line between the header and rest of the body. We also",
        "make sure we don't go beyond the 72 character limit.",
    ]


@pytest.fixture
def message_lines_exceeds_length():
    return [
        "A good commit message header",
        "\n",
        "There is a blank line between the header and rest of the body."
        " We are rambling on.",
        "Make sure we don't go beyond the 72 character limit.",
    ]


@pytest.fixture
def body_lines():
    def message_body(message_lines):
        return message_lines[1:]

    return message_body


@pytest.fixture
def body_with_hyphen_list():
    return [
        "- This is a list",
        "- another bullet point",
        "- there should be a space after the bullet point",
        "- we need to use hanging indent",
        "  so there should be two white spaces",
        "- here's another point",
        "\n",
        "another paragraph...",
    ]


@pytest.fixture
def body_with_star_list():
    return [
        "* This is a list",
        "* another bullet point",
        "* there should be a space after the bullet point",
    ]


@pytest.fixture
def body_with_list_bad_spacing():
    return [
        "* This is a list\n",
        "* with inconsistent use of space\n",
        "*there should be a space after the bullet point\n",
    ]


@pytest.fixture
def body_with_list_bad_indent():
    return [
        "* This is a list",
        "* with not hanging indent",
        "this is not hanging indent",
    ]


@pytest.fixture
def body_with_list_bad_no_blank_line():
    return [
        "* This is a list",
        "* with not hanging indent",
        "another paragraph...",
    ]
