from code_review import average

def test_average_normal():
    assert average([2, 4, 6]) == 4

def test_average_single():
    assert average([7]) == 7

def test_average_empty():
    try:
        average([])
        assert False
    except ValueError:
        assert True

