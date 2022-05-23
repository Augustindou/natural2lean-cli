
red = lambda s: "\u001b[31m" + s + "\u001b[0m"
green = lambda s: "\u001b[32m" + s + "\u001b[0m"
cyan = lambda s: "\u001b[36m" + s + "\u001b[0m"
underline = lambda s: "\u001b[4m" + s + "\u001b[0m"


def string_differences(old: str, new: str) -> str:
    """Adds color to the lines in new that were not in old.

    Args:
        old (str): the old string.
        new (str): the new string.

    Returns:
        str: The new string with
    """
    result = ""

    for line in new.splitlines():
        if line in old:
            result += line + "\n"
        else:
            result += green(line) + "\n"

    return result
