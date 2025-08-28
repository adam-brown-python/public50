from um import count
def main():
    test_count()

def test_count():
    assert count("Um, Mum? is this that album where um, ummm, the clumsy alums play drums?") == 2
    assert count("Hello, um world") == 1
    assert count("Um... what are regular expressions?") == 1

if __name__ == "__main__":
    main()
