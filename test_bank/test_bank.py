from bank import value
import pytest

def test_value_hello():
    #Hello Newman
    assert value("Hello, newman") == 0
    assert value("Hello") == 0
    assert value("hello") == 0

def test_value_h():
    assert value("How you doing") == 20
    assert value("Hi") == 20
    assert value("helo") == 20


def test_value_other():
    assert value("What's happening") == 100
    assert value("Cs50") == 100
    assert value("50") == 100
