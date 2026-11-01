import pytest

from rayid import RayID


def test_digit_generation():
    result = RayID("digit").gen(25)

    assert len(result) == 25
    assert result.isdigit()
    assert result[0] != "0"


def test_lower_generation():
    result = RayID("lower").gen(25)

    assert len(result) == 25
    assert result.islower()
    assert result.isalpha()


def test_upper_generation():
    result = RayID("upper").gen(25)

    assert len(result) == 25
    assert result.isupper()
    assert result.isalpha()


def test_all_generation():
    result = RayID("all").gen(25)

    assert len(result) == 25
    assert result[0] != "0"


def test_invalid_type():
    with pytest.raises(ValueError):
        RayID("invalid")


@pytest.mark.parametrize("length", [0, -1])
def test_invalid_length(length):
    with pytest.raises(ValueError):
        RayID("digit").gen(length)


def test_invalid_length_type():
    with pytest.raises(TypeError):
        RayID("digit").gen("25")
