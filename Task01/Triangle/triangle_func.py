class IncorrectTriangleSides(Exception):
    pass

def get_triangle_type(side1, side2, side3):
    if side1 <= 0 or side2 <= 0 or side3 <= 0 or side1 + side2 <= side3 or side1 + side3 <= side2 or side2 + side3 <= side1:
        raise IncorrectTriangleSides("Incorrect side lengths of a triangle")

    if side1 == side2 == side3:
        return "equilateral"
    elif side1 == side2 or side1 == side3 or side2 == side3:
        return "isosceles"
    else:
        return "nonequilateral"

if __name__ == "__main__":
    import doctest
    doctest.testmod()