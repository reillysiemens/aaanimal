"""Tests for the aaanimal module."""
import pytest

import aaanimal


def test_generate_empty_string():
    """Generate should return the empty string when given zero adjectives and
    zero animals."""
    assert aaanimal.generate(adjectives=0, animals=0) == ""


def test_generate_zero_adjectives(adjectives, animals):
    """TODO"""
    animal = {aaanimal.generate(adjectives=0, animals=1, separator="-")}
    assert animal.isdisjoint(adjectives) and animal.issubset(animals)


def test_generate_zero_animals(adjectives, animals):
    """TODO"""
    adjective = {aaanimal.generate(adjectives=1, animals=0, separator="-")}
    assert adjective.isdisjoint(animals) and adjective.issubset(adjectives)


def test_generate_uses_expected_adjectives_and_animals(adjectives, animals):
    """Generate uses adjectives and animals from the expected set of adjectives
    and animals."""
    separator = "-"

    result = aaanimal.generate(adjectives=2, animals=1, separator=separator)
    adjective1, adjective2, animal = result.split(separator)

    assert {adjective1, adjective2}.issubset(adjectives)
    assert animal in animals


@pytest.mark.parametrize(
    "kwargs",
    (
        pytest.param({"adjectives": "should be an int"}, id="invalid adjectives"),
        pytest.param({"animals": "should be an int"}, id="invalid animals"),
        pytest.param({"separator": 42}, id="invalid separator"),
    ),
)
def test_generate_raises_type_errors(kwargs):
    """Generate raises a TypeError when give arguments with an invalid type."""
    with pytest.raises(TypeError):
        aaanimal.generate(**kwargs)


@pytest.mark.parametrize(
    "kwargs",
    (
        pytest.param({"adjectives": -1}, id="adjectives underflow"),
        pytest.param({"animals": -1}, id="animals underflow"),
    ),
)
def test_generate_disallows_underflow(kwargs):
    """Generate raises an OverflowError indicating that a negative integer
    can't be used where an unsigned integer is expected."""
    with pytest.raises(OverflowError, match="can't convert negative int to unsigned"):
        aaanimal.generate(**kwargs)


@pytest.mark.parametrize(
    "kwargs",
    (
        pytest.param({"adjectives": (2 ** 128) + 1}, id="adjectives overflow"),
        pytest.param({"animals": (2 ** 128) + 1}, id="animals overflow"),
    ),
)
def test_generate_disallows_overflow(kwargs):
    """Generate raises an OverflowError indicating that a Python integer is too
    big to be converted into a Rust integer without overflowing."""
    with pytest.raises(OverflowError, match="int too big to convert"):
        aaanimal.generate(**kwargs)
