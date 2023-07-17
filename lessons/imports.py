"""Examples of importing Python."""


from lessons import helpers

# Alias a module / imported name as another name
from lessons import helpers as hs

#import names defined globally in a module
from lessons.helpers import powerful, THE_ANSWER

def main() -> None:
    """Entrypoint of program."""
    print(helpers.powerful(2, 4))
    print(f"The ansswer: {helpers.THE_ANSWER}")


if __name__ == "__main__":
    main()

