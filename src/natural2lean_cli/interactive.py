from dataclasses import dataclass
from natural2lean import Translator, LeanError, TranslationError, NoConclusion
from InquirerPy import inquirer
from .utils.text import cyan, red, green, underline, string_differences, color_feedback


BACKTRACK = ("BACKTRACK", "BACK")
BACKTRACK_MESSAGE = cyan("โช Backtracking...\n")
NO_BACKTRACK_MESSAGE = red("๐งจ Cannot backtrack anymore, use 'exit' to quit.\n")

EXIT = ("EXIT", "QUIT", "STOP")
EXIT_MESSAGE = cyan("๐ Bye!\n")

GOAL_SOLVED_MESSAGE = green(f"๐ Congratulations, you solved a goal !\n")
ALL_GOALS_SOLVED_MESSAGE = green("๐ Congratulations, you solved all the goals !")
LAST_STATE_MESSAGE = "Here is the last state:"
TRANSLATION_ERROR_MESSAGE = red(
    "๐งจ The system could not understand your statement, try again.\n"
)
LEAN_ERROR_MESSAGE = red(
    "๐งจ Lean could not assert that your statement is correct, try verifying it or take smaller steps.\n"
)
NO_CONCLUSION_MESSAGE = red(
    "๐งจ The system could not conclude a goal at this point, nor match a non-conclusive statement in your input.\n"
)

def interactive():
    translator = Translator()
    last_input = ""

    while True:
        state = translator.state()

        # ask for a statement or a theorem
        if state.goals:
            input = statement_query(default=last_input)
        else:
            input = theorem_query(default=last_input)

        # check for backtrack
        if input.upper() in BACKTRACK:
            if translator.backtrack():
                print(BACKTRACK_MESSAGE)
            else:
                print(NO_BACKTRACK_MESSAGE)
            state = translator.state()
            if state.goals:
                print(LAST_STATE_MESSAGE)
                print(state)
            continue

        # check for exit
        elif input.upper() in EXIT:
            print(EXIT_MESSAGE)
            break

        # translate input
        try:
            last_state = translator.state()
            state = translator.new(input)
            last_input = ""

            # print sentence understanding
            print(color_feedback(translator.interpretation_feedback()) + "\n")
            
            # goals solved
            if not state.goals:
                print(ALL_GOALS_SOLVED_MESSAGE)
            elif len(state.goals) < len(last_state.goals):
                print(GOAL_SOLVED_MESSAGE)

            # print new state
            print(string_differences(str(last_state), str(state)))

        except TranslationError as e:
            print(TRANSLATION_ERROR_MESSAGE)
            last_input = input
            # for testing purposes
            print(e)

        except LeanError as e:
            # how the failed statement was translated
            print(color_feedback(translator.failed_statement_interpretation()) + "\n")
            # error message
            print(LEAN_ERROR_MESSAGE)
            last_input = input
            # for testing purposes
            print(e)

        except NoConclusion as e:
            # how the failed statement was translated
            print(color_feedback(translator.failed_statement_interpretation()) + "\n")
            # error message
            print(NO_CONCLUSION_MESSAGE)
            last_input = input
            # for testing purposes
            print(e)


# ---------- QUERIES ----------


def theorem_query(default="") -> str:
    input = inquirer.text(
        message="Enter a theorem statement.\n ",
        validate=lambda x: x.strip() != "",
        default=default,
    ).execute()

    # spacing
    print()

    return input


def statement_query(default="") -> str:
    input = inquirer.text(
        message="Input a statement.\n ",
        validate=lambda x: x.strip() != "",
        default=default,
    ).execute()

    # spacing
    print()

    return input
