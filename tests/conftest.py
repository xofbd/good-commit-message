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
        "make sure we don't go beyond the 72 character limit."
    ]


@pytest.fixture
def message_lines_no_blank():
    return [
        "A good commit message header\n",
        "There is a blank line between the header and rest of the body. We also\n",
        "make sure we don't go beyond the 72 character limit."
    ]


@pytest.fixture
def message_lines_exceeds_length():
    return [
        "A good commit message header\n",
        "\n",
        "There is a blank line between the header and rest of the body. We are rambling on.\n",
        "Make sure we don't go beyond the 72 character limit."
    ]

@pytest.fixture
def body_lines():
    def message_body(message_lines): 
        return message_lines[1:]

    return message_body
