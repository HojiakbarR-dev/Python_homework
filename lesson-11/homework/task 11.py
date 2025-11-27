# test_script.py
# Run simple tests for your modules and packages

from math_operations import add, subtract, multiply, divide
from string_utils import reverse_string, count_vowels

from geometry import calculate_area, calculate_circumference
from file_operations import read_file, write_file

def test_math():
    print("Math tests:")
    print("1 + 2 =", add(1,2))
    print("5 - 3 =", subtract(5,3))
    print("4 * 3 =", multiply(4,3))
    print("10 / 2 =", divide(10,2))

def test_string():
    s = "Hello, World!"
    print("\nString tests:")
    print("Reverse:", reverse_string(s))
    print("Vowel count:", count_vowels(s))

def test_geometry():
    r = 3
    print("\nGeometry tests:")
    print("Area of circle radius", r, "=", calculate_area(r))
    print("Circumference of circle radius", r, "=", calculate_circumference(r))

def test_file_ops():
    print("\nFile operations tests:")
    path = "sample.txt"
    write_file(path, "This is a sample file.\nLine 2.")
    content = read_file(path)
    print("Read content:\n", content)

if __name__ == "__main__":
    test_math()
    test_string()
    test_geometry()
    test_file_ops()
