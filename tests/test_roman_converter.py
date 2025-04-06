import unittest

from src.roman_converter import decimal_to_roman

class TestRomanConverter(unittest.TestCase):
    def test_basic_number(self):
        self.assertEqual(decimal_to_roman(1),"I")
        self.assertEqual(decimal_to_roman(5),"V")
        self.assertEqual(decimal_to_roman(10),"X")
        self.assertEqual(decimal_to_roman(50),"L")
        self.assertEqual(decimal_to_roman(100),"C")
        self.assertEqual(decimal_to_roman(500),"D")
        self.assertEqual(decimal_to_roman(1000),"M")
    def test_subtraction_rules(self):
        self.assertEqual(decimal_to_roman(4),"IV")
        self.assertEqual(decimal_to_roman(9),"IX")
        self.assertEqual(decimal_to_roman(40),"XL")
        self.assertEqual(decimal_to_roman(90),"XC")
        self.assertEqual(decimal_to_roman(400),"CD")
        self.assertEqual(decimal_to_roman(900),"CM")
    def test_complex_number(self):
        self.assertEqual(decimal_to_roman(49),"XLIX")
        self.assertEqual(decimal_to_roman(99),"XCIX")
        self.assertEqual(decimal_to_roman(499),"CDXCIX")
        self.assertEqual(decimal_to_roman(999),"CMXCIX")
        self.assertEqual(decimal_to_roman(3999),"MMMCMXCIX")
    def test_wrong_number(self):
        self.assertEqual(decimal_to_roman(5000),"Error, el numero debe ser entre 1 y 3999")
        self.assertEqual(decimal_to_roman(4000),"Error, el numero debe ser entre 1 y 3999")
        self.assertEqual(decimal_to_roman(0),"Error, el numero debe ser entre 1 y 3999")
        self.assertEqual(decimal_to_roman(-10),"Error, el numero debe ser entre 1 y 3999")

if __name__ == '__main__':
    unittest.main()
        