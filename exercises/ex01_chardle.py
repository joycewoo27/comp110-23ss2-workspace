"""EX01 - Chardle - A cute step toward Wordle."""

__author__ = "730199211"

word: str = input("Enter a 5-character word. ")
if len(word) != 5:
    print("Error: Word must contain 5 characters")
    exit()

letter: str = input("Enter a single character. ")
if len(letter) != 1:
    print("Error: Character must be single character.")
    exit()
print("Searching for " + letter + " in " + word)

no_instances: int = 0

if word[0] == letter:
    print(letter + " found at index 0")
    no_instances = no_instances + 1
if word[1] == letter:
    print(letter + " found at index 1")
    no_instances = no_instances + 1
if word[2] == letter:
    print(letter + " found at index 2")
    no_instances = no_instances + 1
if word[3] == letter:
    print(letter + " found at index 3")
    no_instances = no_instances + 1
if word[4] == letter:
    print(letter + " found at index 4")
    no_instances = no_instances + 1

if no_instances == 0:
    print("No instances of " + letter + " found in " + word)
if no_instances == 1:
    print("1 instance of " + letter + " found in " + word)
if no_instances > 1:
    print(str(no_instances) + " instances of " + letter + " found in " + word)
