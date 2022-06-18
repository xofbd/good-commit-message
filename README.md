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

## License
This project is distributed under the MIT license. Please see `LICENSE` for more information.
