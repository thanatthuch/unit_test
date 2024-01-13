from src.area import rectangle, triangle



def test_one():
    assert rectangle(5, 2) == 10
    assert rectangle(5, 4.5) == 22.5
    assert triangle(5, 2) == 5