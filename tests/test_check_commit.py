import pytest

from gcm.check_commit_message import (
    alert_errors,
    check_commit_message,
    load_lines,
    validate_body,
    validate_header,
    validate_list
)


@pytest.mark.parametrize("file_handle,expected", [
    ("file_handle_good", "message_lines_good"),
    ("file_handle_comments", "message_lines_comments"),
])
def test_load_lines(file_handle, expected, request):
    """
    GIVEN a file handle to a commit message
    WHEN load_lines is called with the file handle of that file handle
    THEN the list of the lines of the commit message is returned
    """
    file_handle = request.getfixturevalue(file_handle)
    expected = request.getfixturevalue(expected)
    assert load_lines(file_handle) == expected


@pytest.mark.parametrize("header,expected", [
    (
        "Fix bug", {
            "header_capitalization": True,
            "header_length": True,
            "header_punctuation": True,
        }),
    (
        "fix bug",  {
            "header_capitalization": False,
            "header_length": True,
            "header_punctuation": True,
        }),
    (
        "Fix bug.",  {
            "header_capitalization": True,
            "header_length": True,
            "header_punctuation": False,
        }),
    (
        "fix bug.",  {
            "header_capitalization": False,
            "header_length": True,
            "header_punctuation": False,
        }),
    (
        "Fix a bug and keep on trailing off in the commit header.", {
            "header_capitalization": True,
            "header_length": False,
            "header_punctuation": False
        }),
])
def test_validate_header(header, expected):
    """
    GIVEN a good/bad commit message header
    WHEN validate_header is called
    THEN the correct validation is returned
    """
    assert validate_header(header) == expected


@pytest.mark.parametrize("message_lines,expected", [
    (
        "message_lines_good", {
            "blank_line": True,
            "body_lines_length": True,
        }),
    (
        "message_lines_no_blank", {
            "blank_line": False,
            "body_lines_length": True,
        }),
    (
        "message_lines_exceeds_length", {
            "blank_line": True,
            "body_lines_length": False,
        }),
    (
        "message_lines_no_body", {
             "blank_line": True,
             "body_lines_length": True,
        }),
])
def test_validate_body(message_lines, expected, body_lines, request):
    """
    GIVEN a list of lines of the body of a good commit
    WHEN valid_body is called with the body lines
    THEN True is returned
    """
    message_lines = request.getfixturevalue(message_lines)
    assert validate_body(body_lines(message_lines)) == expected


@pytest.mark.parametrize("body,expected", [
    ("body_with_hyphen_list", {"body_list": True}),
    ("body_with_star_list", {"body_list": True}),
    ("body_with_list_bad_spacing", {"body_list": False}),
    ("body_with_list_bad_indent", {"body_list": False}),
    ("body_with_list_bad_no_blank_line", {"body_list": False}),
])
def test_validate_list(body, expected, request):
    """
    GIVEN the body of a commit message
    WHEN validate_list is called
    THEN the correction validation is returned
    """
    body = request.getfixturevalue(body)

    assert validate_list(body) == expected


@pytest.mark.parametrize("path,status_code", [
    ("path_good", 0),
    ("path_bad", 1),
])
def test_check_commit_message(path, status_code, request):
    """
    GIVEN a path to commit message
    WHEN the check_commit_message function is called with the file handle of that path
    THEN the script exists with the correct exit code
    """
    path = request.getfixturevalue(path)

    with open(path, "r") as f:
        assert check_commit_message(f) == status_code


@pytest.mark.parametrize(
    "test_results,outputs",
    [
        ({"header_capitalization": True, "body_list": True}, []),
        (
            {"header_capitalization": True, "body_list": False},
            ["* Lists in commit body are not formatted properly"]
        ),
        (
            {"header_capitalization": False, "body_list": False},
            [
                "* Header should use sentence capitalization",
                "* Lists in commit body are not formatted properly"
            ]),
    ]
)
def test_alert_errors(test_results, outputs, capsys):
    """
    GIVEN a dictionary of test results
    WHEN alert_errors is called
    THEN if a test failed, the appropriate message is sent to stdout
    """
    alert_errors(test_results)
    stdout = capsys.readouterr().err

    if outputs:
        assert "Commit message was rejected because" in stdout
        assert "To skip the check, run:" in stdout
        assert "To recover your previous commit message, run:" in stdout
    else:
        assert not stdout

    for output in outputs:
        assert output in stdout
