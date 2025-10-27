from calculator import add

def test_add_integers():
    assert add(2, 3) == 5

def test_add_floats():
    assert abs(add(2.5, 3.2) - 5.7) < 0.0001
