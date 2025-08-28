from working import convert
import pytest
def main():
    test_convert()

def test_convert():
    with pytest.raises(ValueError):
        convert("9:00 AM 5:00 PM")
    with pytest.raises(ValueError):
        convert("9:00 AM - 5:00 PM")
    with pytest.raises(ValueError):
        convert("09:60 AM to 5:00 PM")
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
    assert convert("5:30 AM to 6:30 PM") == "05:30 to 18:30"

if __name__ == "__main__":
    main()
