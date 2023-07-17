"""CQ15 - Count the differences."""


def differences(a: list[int], b: list[int]) -> int:
    """Count the differences between two lists."""
    result: int = 0
    short: list[int]
    if len(a) >= len(b):
        result = len(a) - len(b)
        short = b
    else:
        result = len(b) - len(a)
        short = a

    i: int = 0
    while i < len(short):
        if a[i] != b[i]:
            result += 1
        i += 1

    return result


xs: list[int] = [1, 3, 3, 4, 5]
ys: list[int] = [1, 2, 3]
print(differences(xs, ys))



