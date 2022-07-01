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

## Installation
This project just uses the Python standard library so no 3rd party packages are required for installation. Thus, there is no need for a tool like [pipx](https://pypa.github.io/pipx/). However, for development work, it does rely on 3rd party packages.

To install, run:
```bash
pip install git+https://github.com/xofbd/good-commit-message
```
or
```
git clone https://github.com/xofbd/good-commit-message
pip install good-commit-message
```
Note: you can use the `--user` flag for a local installation as opposed to system-wide.

The installation will add `check-commit-message` script but you'll need to link it to your project's `commit-msg`, located in `.git/hooks`. You can follow the script `bin/install-hook` or run it (if you've cloned the repo and have not navigated away):
```
good-commit-message/bin/install-hook <path-to-git-project>
```

If you are already using `commit-msg`, you can just edit that file to call `check-commit-messsage` as part of a larger message checking process.

## Usage
With the script linked to your projects `commit-msg`, the hooks is run after creating the commit's message. If a commit message is rejected, you'll be informed either how to skip the check or to retrieve the rejected message so you can edit it and try again.

## License
This project is distributed under the MIT license. Please see `LICENSE` for more information.
