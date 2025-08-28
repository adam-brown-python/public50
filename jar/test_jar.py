from jar import Jar
def test_withdraw():
    jar = Jar()
    jar.deposit(5)
    jar.withdraw(1)
    assert jar.__str__() == "🍪🍪🍪🍪"

def test_deposit():
    jar2 = Jar()
    jar2.deposit(5)
    assert jar2.__str__() == "🍪🍪🍪🍪🍪"

def test_init():
    jar3 = Jar()
    assert jar3.__str__() == ""

def test_str():
    jar4 = Jar()
    assert jar4.__str__() == ""
