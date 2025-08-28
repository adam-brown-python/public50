import pytest
from fuel import convert,gauge
def main():
    test_e()
    test_convert()
    test_gauge()

def test_e():
    with pytest.raises(ValueError):
        convert("cat/dog")
    with pytest.raises(ZeroDivisionError):
        convert("1/0")
    with pytest.raises(ValueError):
        convert('-1/2')

def test_convert():
    assert convert("1/2") == 50
    assert convert("1/4") == 25

def test_gauge():
    assert gauge(50)== "50%"
    assert gauge(1) == "E"
    assert gauge(99) == "F"
    assert gauge(25) == "25%"

if __name__ == "__main__":
    main()
