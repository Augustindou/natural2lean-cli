from pathlib import Path
from natural2lean import Translator, LeanError, TranslationError, NoConclusion
from .utils.text import red, green, cyan
from .utils.progress_indicator import ProgressIndicator


def file(path: Path):
    translator = Translator()
    state = None

    with open(path, "r") as f:
        lines = f.readlines()
        n_lines = len(lines)

    progressbar = ProgressIndicator(30)

    for i, line in enumerate(lines):
        progressbar.update(i / n_lines)
        # skip empty lines
        if line.strip() == "":
            continue

        try:
            # feed line
            state = translator.new(line)

        except TranslationError as e:
            print_error(f"The system could not understand line {i+1}.", e, state)
            raise e

        except LeanError as e:
            print_error(f"Lean could not assert the validity of line {i+1}.", e, state)
            raise e

        except NoConclusion as e:
            print_error(
                f"The system could not conclude a goal at line {i+1}, nor match a non-conclusive statement in your input.",
                e,
                state,
            )
            raise e

    progressbar.finish()

    if state.goals:
        print(
            cyan(
                "\n🚀 Your statements are valid, but there are still goals to be solved. Here's the state after parsing the whole file:\n"
            )
        )
        print(state)
    else:
        print(green("\n🚀 Congratulations, you solved all the goals !"))


def print_error(message, e, state):
    print(red(f"\n🧨 {message}"))
    print(f"Error: {e}\n")
    print("Here's the state of the system before the error occured:\n")
    print(state)
