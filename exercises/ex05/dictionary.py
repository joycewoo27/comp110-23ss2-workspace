"""EX05 - Dictionary."""

__author__ = "730199211"


def invert(x: dict[str, str]) -> dict[str, str]:
    """Inverts the keys and the values given a dictionary of [str, str]."""
    result: dict[str, str] = {}
    
    for key in x:
        for value in result:
            if x[key] == value:
                raise KeyError("Duplicate Keys")
        result[x[key]] = key
    return result


def favorite_color(colors: dict[str, str]) -> str:
    """Returns color that occurs the most.""" 
    favColor: str = ""
    count: int = 0
    colors1: dict[str, int] = {}
    for name in colors:
        if colors[name] in colors1:
            colors1[colors[name]] = colors1[colors[name]] + 1
        else: 
            colors1[colors[name]] = 1
    for name in colors1:
        if colors1[name] > count:
            favColor = name
            count = colors1[name]
    return favColor


def count(x: list[str]) -> dict[str, int]:
    """Returns dictionary with counts of each item in given list."""
    count: dict[str, int] = {}
    for key in x:
        if key in count:
            count[key] += 1
        else:
            count[key] = 1
    return count
