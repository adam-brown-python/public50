from plates import is_valid

def main():
    test_plates()

def test_plates():
    assert is_valid("50") == False
    assert is_valid("CS50") == True
    assert is_valid("PI3.14") == False
    assert is_valid("H") == False
    assert is_valid("HELLO") == True
    assert is_valid("one, two ") == False
    assert is_valid("cs50p") == False
    assert is_valid("Cs05") == False

if __name__ == "__main__":
    main()

