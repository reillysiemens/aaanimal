"""Tests for the aaanimal module."""
import pytest

from aaanimal import generate


def test_generate_empty_string():
    """Generate should return the empty string when given zero adjectives and
    zero animals."""
    assert generate(adjectives=0, animals=0) == ""


def test_generate_alternative_separator():
    """Generate should be capable of using an alternative separator."""
    separator = "•"
    result = generate(adjectives=2, animals=1, separator=separator)
    assert len(result.split(separator)) == 3


@pytest.mark.parametrize(
    "num_animals",
    (
        pytest.param(1, id="one animal"),
        pytest.param(2, id="two animals"),
    ),
)
def test_generate_zero_adjectives(num_animals, adjectives, animals):
    """Generate should not include extraneous separators in the output when
    there are zero adjectives."""
    separator = "-"
    result = set(
        generate(
            adjectives=0,
            animals=num_animals,
            separator=separator,
        ).split(separator)
    )
    assert result.isdisjoint(adjectives) and result.issubset(animals)


@pytest.mark.parametrize(
    "num_adjectives",
    (
        pytest.param(1, id="one adjective"),
        pytest.param(2, id="two adjectives"),
    ),
)
def test_generate_zero_animals(num_adjectives, adjectives, animals):
    """Generate should not include extraneous separators in the output when
    there are zero animals."""
    separator = "-"
    result = set(
        generate(
            adjectives=num_adjectives,
            animals=0,
            separator=separator,
        ).split(separator)
    )
    assert result.isdisjoint(animals) and result.issubset(adjectives)


def test_generate_uses_expected_adjectives_and_animals(adjectives, animals):
    """Generate should use adjectives and animals from the expected set of
    adjectives and animals."""
    separator = "-"

    result = generate(adjectives=2, animals=1, separator=separator)
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
    """Generate should raise a TypeError when give arguments with an invalid
    type."""
    with pytest.raises(TypeError):
        generate(**kwargs)


@pytest.mark.parametrize(
    "kwargs",
    (
        pytest.param({"adjectives": -1}, id="adjectives underflow"),
        pytest.param({"animals": -1}, id="animals underflow"),
    ),
)
def test_generate_disallows_underflow(kwargs):
    """Generate should raise an OverflowError indicating that a negative
    integer can't be used where an unsigned integer is expected."""
    with pytest.raises(OverflowError, match="can't convert negative int to unsigned"):
        generate(**kwargs)


@pytest.mark.parametrize(
    "kwargs",
    (
        pytest.param({"adjectives": (2 ** 128) + 1}, id="adjectives overflow"),
        pytest.param({"animals": (2 ** 128) + 1}, id="animals overflow"),
    ),
)
def test_generate_disallows_overflow(kwargs):
    """Generate should raise an OverflowError indicating that a Python integer
    is too big to be converted into a Rust integer without overflowing."""
    with pytest.raises(OverflowError, match="int too big to convert"):
        generate(**kwargs)
