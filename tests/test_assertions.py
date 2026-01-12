from assertions import withdraw

def test_withdraw_normal():
    assert withdraw(100, 40) == 60

def test_withdraw_exact():
    assert withdraw(50, 50) == 0

def test_withdraw_too_much():
    try:
        withdraw(50, 100)
        assert False
    except ValueError:
        assert True