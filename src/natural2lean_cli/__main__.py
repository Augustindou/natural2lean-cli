from natural2lean import update_git
from pathlib import Path
import argparse
from InquirerPy import inquirer
from InquirerPy.validator import PathValidator
from .interactive import interactive
from .file import file

is_interactive = lambda mode: mode in ["interactive", "i"]
is_file = lambda mode: mode in ["file", "f"]
is_cli = lambda mode: mode in ["full_cli", "cli"]
is_update = lambda mode: mode == "update"


def main():
    mode, input_file = parse_args()
    
    # ambiguous because interactive mode and file given
    if not is_file(mode) and input_file != None:
        print(f"Should not specify input file in {mode} mode.")
        mode = "full_cli"

    # update if asked
    if is_update(mode):
        update_git()

    # ask for file if not specified
    if is_file(mode) and input_file is None:
        input_file = file_query()

    # full cli
    if is_cli(mode):
        mode = mode_query()
        if is_file(mode):
            input_file = file_query()

    # file mode
    if is_file(mode):
        file(input_file)

    # interactive mode
    if is_interactive(mode):
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
