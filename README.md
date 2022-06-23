![Python](https://shields.io/badge/Python-3.7%20%7C%203.8%20%7C%203.9%20%7C%203.10-blue)
[![GitHub release](https://img.shields.io/github/v/release/xofbd/good-commit-message.svg)](https://github.com/xofbd/good-commit-message.svg/releases)
[![License: MIT](https://img.shields.io/github/license/xofbd/good-commit-message)](https://opensource.org/licenses/MIT)
![CI](https://github.com/xofbd/good-commit-message/workflows/CI/badge.svg?branch=master)
[![codecov](https://codecov.io/gh/xofbd/good-commit-message/branch/master/graph/badge.svg?token=FIAVAEQ60L)](https://codecov.io/gh/xofbd/good-commit-message)
# Commit Message Linter
A simple Python script that checks whether a commit's message follows these conventions:
1. Sentence capitalization of the first line
1. The first line does not exceed 50 characters
1. The first line does not end in a period
1. A blank line between a commit's first line and the rest of the body
1. The rest of the lines do not exceed 72 characters
1. Any lists either use a hyphen (-) or asterisk (*) with hanging indent when the point spans more than one line

These conventions are common and mostly adapted from [here](https://tbaggery.com/2008/04/19/a-note-about-git-commit-messages.html)

## Usage
The linter script is meant to be used as a project's Git hook. Link or place `gcm/check_commit.py` as `.git/hooks/commit-msg` for your project.

If a commit message is rejected, you'll be informed either how to skip the check or to retrieve the rejected message (Based on https://salferrarello.com/recover-failed-git-commit-message/).

## License
This project is distributed under the MIT license. Please see `LICENSE` for more information.
