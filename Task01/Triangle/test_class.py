import pytest

from triangle_class import IncorrectTriangleSides, Triangle

def test_triangle_creation():
    triangle = Triangle(3, 4, 5)
    assert triangle.side1 == 3
    assert triangle.side2 == 4
    assert triangle.side3 == 5

def test_triangle_type_equilateral():
    triangle = Triangle(6, 6, 6)
    assert triangle.triangle_type() == "equilateral"

def test_triangle_type_isosceles():
    triangle = Triangle(10, 10, 6)
    assert triangle.triangle_type() == "isosceles"

def test_triangle_type_nonequilateral():
    triangle = Triangle(12, 7, 15)
    assert triangle.triangle_type() == "nonequilateral"

def test_triangle_creation_negative_side():
    with pytest.raises(IncorrectTriangleSides):
        Triangle(1, 13, 4)

def test_triangle_creation_impossible_triangle():
    with pytest.raises(IncorrectTriangleSides):
        Triangle(21, -1, 8)

def test_triangle_creation_zero_side():
    with pytest.raises(IncorrectTriangleSides):
        Triangle(0, 1, 2)

def test_triangle_perimeter():
    triangle = Triangle(3, 4, 5)
    assert triangle.perimeter() == 12

def test_triangle_perimeter_equilateral():
    triangle = Triangle(5, 5, 5)
    assert triangle.perimeter() == 15