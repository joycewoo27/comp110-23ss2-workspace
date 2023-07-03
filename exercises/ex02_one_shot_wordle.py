"""One shot wordle."""

__author__ = "730199211"

# declaring variables for establishing secret and prompting for a guess
secret: str = "python"
number: int = len(secret)
guess: str = input(f"What is your {number}-letter guess? ")

# reassigning a variable to be the result of prompting for input again
while len(guess) != number:
    guess = input(f"That was not {number} letters! Try again: ")

# emojis
WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"

# checking indices for correct matches
if len(guess) == number:
    first: int = 0
    box: str = ""
    while first < number:
        if guess[first] == secret[first]:
            box = box + GREEN_BOX
        else:
            # CURRENT INDEX DOESN'T MATCH SAME INDEX OF SECRET
            # declare a boolean variable to keep track of yellow letters
            exist: bool = False
            alt: int = 0
            while exist != True and alt < number:
                # does alternate index of the secred word = current index of guessed word?
                if guess[first] == secret[alt]:
                    exist = True
                else:
                    alt = alt + 1
            if exist is True:
                box = box + YELLOW_BOX
            else:
                box = box + WHITE_BOX
        first = first + 1
print(box)

# error message if guess is 6 letters but incorrect (displayed after emojis)
if guess != secret and len(guess) == number:
    print("Not quite. Play again soon! ")

if guess == secret:
    print("Woo! You got it! ")