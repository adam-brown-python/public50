from tutorial import calculator
import pytest

def test_calculator():
    assert calculator(1,2) == 3
    assert calculator(3,4) == 7
    assert calculator(5,5) == 10
def test_err():
    with pytest.raises(ValueError):
        calculator("hi","bye")
    with pytest.raises(TypeError):
        calculator("hi")

