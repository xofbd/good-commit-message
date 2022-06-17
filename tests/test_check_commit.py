import pytest

from gcm.check_commit import load_lines, main, validate_body, validate_header


def test_load_lines(path_good, message_lines_good):
    """
    GIVEN a path to a commit message
    WHEN load_lines is called with the path
    THEN the list of the lines of the commit message is returned
    """
    assert load_lines(path_good) == message_lines_good


@pytest.mark.parametrize("header,expected", [
    ("Fix bug", True),
    ("fix bug", False),
    ("Fix bug.", False),
    ("fix bug.", False),
    ("Fix a bug and keep on trailing off in the commit header.", False),
])
def test_validate_header(header, expected):
    """
    GIVEN a good/bad commit message header
    WHEN validate_header is called
    THEN the correct validation is returned
    """
    assert validate_header(header) == expected


@pytest.mark.parametrize("message_lines,expected", [
    ("message_lines_good", True),
    ("message_lines_no_blank", False),
    ("message_lines_exceeds_length", False),
])
def test_validate_body(message_lines, expected, body_lines, request):
    """
    GIVEN a list of lines of the body of a good commit
    WHEN valid_body is called with the body lines
    THEN True is returned
    """
    message_lines = request.getfixturevalue(message_lines)
    assert validate_body(body_lines(message_lines)) == expected


@pytest.mark.parametrize("path,status_code,message", [
    ("path_good", 0, ""), ("path_bad", 1, "Commit message did not meet the convention\n")
])
def test_main(path, status_code, message, capsys, request):
    """
    GIVEN a path to commit message
    WHEN the main function is called
    THEN the script exists with the correct exit code and output to STDERR
    """
    path = request.getfixturevalue(path)

    with pytest.raises(SystemExit) as error:
        main(path)

    assert error.type == SystemExit
    assert error.value.code == status_code
    assert capsys.readouterr().err == message
