from natural2lean import update_git
from pathlib import Path
import argparse
from InquirerPy import inquirer
from InquirerPy.validator import PathValidator
from .interactive import interactive
from .file import file
from .utils.text import red

KEYWORDS = {
    "interactive": ("interactive", "i"),
    "file": ("file", "f"),
    "cli": ("full_cli", "full", "cli"),
    "update": ("update", "u"),
}

def main():
    mode, input_file = parse_args()

    # invalid mode
    if mode not in [v for kwds in KEYWORDS.values() for v in kwds]:
        print(red("Invalid argument, mode can be 'interactive' or 'file'. Please use the following CLI to choose your mode. You can also run 'natural2lean update' to get the latest version of the project template."))
        mode = "full_cli"
    
    # ambiguous because interactive mode and file given
    if mode not in KEYWORDS["file"] and input_file != None:
        print(f"Should not specify input file in {mode} mode.")
        mode = "full_cli"

    # update if asked
    if mode in KEYWORDS["update"]:
        update_git()

    # ask for file if not specified
    if mode in KEYWORDS["file"] and input_file is None:
        input_file = file_query()

    # full cli
    if mode in KEYWORDS["cli"]:
        mode = mode_query()
        if mode in KEYWORDS["file"]:
            input_file = file_query()

    # file mode
    if mode in KEYWORDS["file"]:
        file(input_file)

    # interactive mode
    if mode in KEYWORDS["interactive"]:
        interactive()


def mode_query() -> str:
    return inquirer.select(
        message="What mode do you want to use?",
        choices=["interactive", "file"],
        default="interactive",
    ).execute()


def file_query() -> Path:
    return inquirer.filepath(
        message="Which file do you want to use?",
        validate=PathValidator(is_file=True, message="Invalid path"),
    ).execute()


def parse_args() -> tuple[str, argparse.FileType]:
    parser = argparse.ArgumentParser(description="natural2lean")
    parser.add_argument(
        "mode",
        type=str,
        nargs="?",
        default="full_cli",
        help='Program mode. Can be either "interactive" or "file". You can also run "natural2lean update" to get the latest version of the project template.',
    )
    parser.add_argument(
        "input_file",
        type=Path,
        nargs="?",
        default=None,
        help="Input file for file mode.",
    )
    args = parser.parse_args()

    return args.mode, args.input_file
