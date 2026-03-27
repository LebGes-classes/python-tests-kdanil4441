import pytest
from math_utils import add, subtract, multiply, divide, create_data


@pytest.fixture
def numbers():
    return create_data()


def test_add():
    assert add(2, 3) == 5
    assert add(-5, 3) == -2
    assert add(0, 0) == 0
    assert add(-10, -15) == -25
    assert round(add(3.14, 2.86), 7) == 6.0
    assert round(add(-1.5, 1.5), 7) == 0.0
    assert add(1000000, 1) == 1000001
    assert round(add(0.0001, 0.0009), 7) == 0.001


def test_subtract():
    assert subtract(10, 4) == 6
    assert subtract(5, 8) == -3
    assert subtract(0, 0) == 0
    assert subtract(-5, -3) == -2
    assert round(subtract(7.5, 2.5), 7) == 5.0
    assert round(subtract(3.14, 1.14), 7) == 2.0
    assert round(subtract(100, 99.9), 7) == 0.1
    assert subtract(-10, 5) == -15
    with pytest.raises(TypeError):
        subtract("10", 5)
    with pytest.raises(TypeError):
        subtract(15, "5")
    assert subtract(0, -5) == 5


def test_multiply():
    assert multiply(3, 0) == 0
    assert multiply(3, 5) == 15
    assert multiply(-3, -1) == 3
    assert multiply(-13, 2) == -26
    assert round(multiply(-1.6, -2.5), 7) == 4.0
    assert multiply(-2, 3) == -6
    assert round(multiply(5.2, 2), 7) == 10.4
    assert multiply(3, 4) == 12
    assert multiply(10, 0) == 0
    assert round(multiply(0.5, 0.5), 7) == 0.25


def test_divide():
    assert divide(10, 2) == 5.0
    assert divide(7, 2) == 3.5
    assert divide(0, 5) == 0.0
    assert divide(-10, 2) == -5.0
    assert divide(10, -2) == -5.0
    assert divide(-10, -2) == 5.0
    with pytest.raises(ZeroDivisionError):
        divide(5, 0)
    assert round(divide(7.5, 2.5), 7) == 3.0
    assert divide(1, 3) == pytest.approx(0.3333333333333333)
    with pytest.raises(TypeError):
        divide("10", 2)
    with pytest.raises(TypeError):
        divide(10, "2")
    with pytest.raises(ZeroDivisionError):
        divide(0, 0)


def test_with_fixture(numbers):
    a, b = numbers
    assert add(a, b) == 5