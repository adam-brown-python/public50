from seasons import convert
import pytest
def main():
    test_convert()

def test_convert():
    assert convert(15086880) == "Fifteen million, eighty-six thousand, eight hundred eighty"
    assert convert(525600) == "Five hundred twenty-five thousand, six hundred"

if __name__ == "__main__":
    main()

