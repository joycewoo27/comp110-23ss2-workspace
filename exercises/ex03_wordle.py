"""Wordle. """

__author__ = "730199211"

# Part 1. Declaring function: contains_char
def contains_char(word: str, letter: str) -> bool:
    """Returns True if a character in the second string is found at any index of first string. """
    assert len(letter) == 1
    index: int = 0
    while index < len(word):
        if word[index] == letter:
            return True
        else:
            index = index + 1
    return False

# Part 2. Declaring function: emojified
def emojified(guess: str, secret: str) -> str:
    """Returns a string of emoji whose color codifies for each letter in word. """
    assert len(guess) == len(secret)
    index: int = 0
    box: str = ""
    # emojis
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"
    while index < len(secret):
        if guess[index] == secret[index]:
            box = box + GREEN_BOX
        else:
            exist: bool = False
            exist = False
            # abstraction! contains_char can replace while loop
            if contains_char(secret, guess[index]) is True and exist is False:
                box = box + YELLOW_BOX
            else:
                box = box + WHITE_BOX
        index = index + 1
    return box

# Part 3. Declaring function: input_guess
def input_guess(expected: int) -> str:
    """Prompts user for a guess until guess of expected length is provided. """
    actual: str = input(f"Enter a {expected} character word: ")
    while len(actual) != expected:
        actual =(input(f"That wasn't {expected} chars! Try again: "))
    return actual

# Part 4. Declaring function: main
def main() -> None:
    """The entrypoint of the program and main game loop."""
    secret: str = "codes"
    i: int = 1
    guessed: str = ""
    while i <= 6:
        print(f"=== Turn {i}/6 === ")
        guessed = input_guess(5)
        print(emojified(guessed,secret))
        if guessed == secret:
            print(f"You won in {i}/6 turns! ")
            i = 7
        else:
            i = i + 1
    if guessed != secret:
        print("X/6 - Sorry, try again tomorrow! ")

if __name__ == "__main__":
    main()
