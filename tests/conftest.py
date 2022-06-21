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
        "A good commit message header\n",
        "\n",
        "There is a blank line between the header and rest of the body. We also\n",
        "make sure we don't go beyond the 72 character limit.\n",
        "\n",
        "- We can also support lists\n",
        "- just make sure we have a space between\n",
        "- either a hyphen or asterisk\n",
        "\n",
        "Here's another paragraph. We can also have more than one.\n",
        "\n",
        "* asterisks are allowed\n",
        "* for lists\n",
    ]


@pytest.fixture
def message_lines_no_blank():
    return [
        "A good commit message header\n",
        "There is a blank line between the header and rest of the body. We also\n",
        "make sure we don't go beyond the 72 character limit.",
    ]


@pytest.fixture
def message_lines_exceeds_length():
    return [
        "A good commit message header\n",
        "\n",
        "There is a blank line between the header and rest of the body."
        " We are rambling on.\n",
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
        "- This is a list\n",
        "- another bullet point\n",
        "- there should be a space after the bullet point\n",
        "- we need to use hanging indent\n",
        "  so there should be two white spaces\n",
        "- here's another point\n",
        "\n",
        "another paragraph...\n",
    ]


@pytest.fixture
def body_with_star_list():
    return [
        "* This is a list\n",
        "* another bullet point\n",
        "* there should be a space after the bullet point\n",
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
        "* This is a list\n",
        "* with not hanging indent\n",
        "this is not hanging indent\n",
    ]


@pytest.fixture
def body_with_list_bad_no_blank_line():
    return [
        "* This is a list\n",
        "* with not hanging indent\n",
        "another paragraph...\n",
    ]
