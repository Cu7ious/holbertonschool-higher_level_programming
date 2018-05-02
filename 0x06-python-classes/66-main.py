#!/usr/bin/python3
Square = __import__('6-square').Square

try:
    my_square_1 = Square("lol")
    my_square_1.my_print()
except:
    print("Passed: Square(\"lol\")")
print("--")

try:
    my_square_1 = Square(2, [2, 2])
    my_square_1.my_print()
except:
    print("Passed: Square(2, [2, 2])")
print("--")

try:
    my_square_1 = Square(2, ("2", 2))
    my_square_1.my_print()
except:
    print("Passed: Square(2, (\"2\", 2))")
print("--")

try:
    my_square_1 = Square(2, (2, "2"))
    my_square_1.my_print()
except:
    print("Passed: Square(2, (2, \"2\"))")
print("--")

try:
    my_square_1 = Square(2, (-2, 2))
    my_square_1.my_print()
except:
    print("Passed: Square(2, (-2, 2))")
print("--")

try:
    my_square_1 = Square(2, (2, -2))
    my_square_1.my_print()
except:
    print("Passed: Square(2, (2, -2))")
print("--")

try:
    my_square_1 = Square(2, (2, 2, 2))
    my_square_1.my_print()
except:
    print("Passed: Square(2, (2, 2, 2))")
print("--")

try:
    my_square_1 = Square(2, (2))
    my_square_1.my_print()
except:
    print("Passed: Square(2, (2))")
print("--")

try:
    my_square_1 = Square(0, (2, 3))
    my_square_1.my_print()
except:
    print("Passed: Square(2, (2))")
print("--")
