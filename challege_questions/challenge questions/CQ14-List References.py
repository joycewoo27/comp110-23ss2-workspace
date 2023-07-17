"""CQ14 Move back."""


def main() -> None:
    message: list[str] = ["T", "G","D", "H"]
    moveBack(message, 0)
    moveBack(message, 2)
    print(message)


def moveBack(xs: list[str], index: int) -> None:
    temp: str = xs[index]
    xs[index] = xs[index + 1]
    xs[index +1] = temp


if __name__ == "__main__":
    main()

