"""Dictionary Functions Test."""

__author__ = "730199211"


from exercises.ex05.dictionary import invert
from exercises.ex05.dictionary import favorite_color
from exercises.ex05.dictionary import count


# Unit Tests for invert function
def test_invert_empty() -> None:
    """Edge case for invert: Tests if invert function returns empty dict when input is empty."""
    x: dict[str, str] = {}
    assert invert(x) == {}


def test_invert_single_item() -> None:
    """Use case for invert: Tests if invert function works with one item."""
    x: dict[str, str] = {'apple': 'cat'}
    assert invert(x) == {'cat': 'apple'}


def test_invert_many_items() -> None:
    """Use case for invert: Tests if invert function works with many items."""
    x: dict[str, str] = {'a': 'z', 'b': 'y', 'c': 'x'}
    assert invert(x) == {'z': 'a', 'y': 'b', 'x': 'c'}


# Unit Tests for favorite_color function
def test_favorite_color_empty() -> None:
    """Edge case for favorite_color: Tests if favorite_color function returns empty str when input is empty."""
    colors: dict[str, int] = {}
    assert favorite_color(colors) == ""


def test_favorite_color_many_items() -> None:
    """Use case for favorite_color: Tests if favorite_color function works when there is most frequent color."""
    colors: dict[str, int] = {"Joyce": "purple", "Exra": "purple", "John": "yellow"}
    assert favorite_color(colors) == "purple"


def test_favorite_color_tied_items() -> None:
    """Use case for favorite_color: Tests if favorite_color function returns color that appeared in dictionary first when there is a tie."""
    colors: dict[str, int] = {"Joyce": "purple", "Ezra": "purple", "John": "yellow", "Jun": "yellow"}
    assert favorite_color(colors) == "purple"


# Unit Tests for count function
def test_count_empty() -> None:
    """Edge case for count: Tests if count function returns empty dict when input list is empty."""
    x: list[str] = []
    assert count(x) == {}


def test_count_single_item() -> None:
    """Use case for count: Tests if count function returns dict with one item given one item in list."""
    x: list[str] = ["one"]
    assert count(x) == {"one": 1}


def test_count_multiple_items() -> None:
    """Use case for count: Tests if count function returns dict with one item given one item in list."""
    x: list[str] = ["one", "two", "two", "three", "three", "three", "four", "four", "four", "four"]
    assert count(x) == {"one": 1, "two": 2, "three": 3, "four": 4}
