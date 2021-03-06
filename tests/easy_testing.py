import pyperclip
from InquirerPy import inquirer

green = lambda s: "\u001b[32m" + s + "\u001b[0m"

EXAMPLES = {
    "squares and evenness": [
        r"Theorem Square of even number is even: if $m \in \mathbb{N}$ is even, then $m^2$ is even.",
        r"By definition, if $m$ is even, we have a natural number $n$ such that $m = 2n$.",
        r"Therefore we have $m^2 = (2n)^2 = 4n^2 = 2(2n^2)$.",
        r"Hence, $m^2$ is even.",
    ],
    "q mod 3 is 1": [
        r"Theorem Square mod 3: If $q$ is a natural not divisible by $3$, then $q^2 \mod 3 = 1$.",
        r"Considering the different possibilities of the modulo operation, we have $q \mod 3 \in \{ 0, 1, 2 \}$",
        r"For the first case, as $q$ is not divisible by $3$, we have a contradiction for $0$.",
        r"For the second case, we have $q \mod 3 = 1$",
        r"By definition of the modulo operation, we have $k \in \mathbb{N}$ such that $q = 3k + 1$",
        r"By expansion, we have $q^2 = (3k+1)^2 = 9k^2+6k+1 = 3(3k^2 + 2k) + 1$",
        r"hence, we have $q^2 \mod 3 = 1$",
        r"For the last case, by definition of the modulo operation, we have $k \in \mathbb{N}$ such that $q = 3k + 2$",
        r"Following the same expansion, we have $q^2 = (3k+2)^2 = 3(3k^2+4k+1) +1$",
        r"Hence, we have $q^2 \mod 3 = 1$ again",
    ],
    "contrapositive": [
        r"Theorem square of q divisible by 3 means q is divisible by 3: If $q \in \mathbb{N}$ and $q^2$ is divisible by $3$, then $q$ is also divisible by $3$.",
        r"We will prove the contrapositive",
        r'By the "square mod 3" theorem, we have $q^2 \mod 3 = 1$',
        r"Hence $q^2$ is not divisible by $3$.",
    ],
    "induction": [
        r"For any natural number $n$, $n^3 + 2n$ is divisible by $3$.",
        r"We will use induction on $n$.",
        r"The base case, $n = 0$, is trivial.",
        r"For $n = k+1$, the induction hypothesis gives us that $k^3 + 2k$ is divisible by $3$.",
        r"Therefore, we have a natural number $z$ such that $k^3 + 2k = 3*z$.",
        r"By expansion, we can derive $(k+1)^3 + 2(k+1) = k^3 + 3k^2 + 5k + 3 = k^3 + 2k + 3(k^2 + k + 1) =3z + 3(k^2 + k + 1) = 3(z+k^2+k+1)$.",
        r"Hence, $(k+1)^3 + 2(k+1)$ is divisible by $3$, therefore $n^3 + 2n$ is divisible by $3$,",
    ],
}


if __name__ == "__main__":
    print()

    examples_titles = [ex for ex in EXAMPLES]
    choice = inquirer.select(
        message="Which theorem do you want to test?",
        choices=examples_titles,
    ).execute()

    statements = EXAMPLES[choice]

    pyperclip.copy(statements[0])
    print("\n" + green("copied theorem statement: \n  ") + green(statements[0]) + "\n")

    i = 1

    while True:
        choice = inquirer.select(
            message="What do you want to copy?",
            choices=statements,
            default=statements[i],
        ).execute()

        # copy to clipboard
        pyperclip.copy(choice)
        print("\n" + green("copied statement: \n  ") + green(choice) + "\n")

        # get next position in list
        i = statements.index(choice) + 1

        # break when all statements are copied
        if i == len(statements):
            break
