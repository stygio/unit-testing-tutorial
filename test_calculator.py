# Unit tests for the calculator library

import unittest
import calculator

class TestCalculator(unittest.TestCase):

	def test_add(self):
		self.assertEqual(calculator.add(3, 4), 7)
		self.assertEqual(calculator.add(3, -4), -1)
		self.assertEqual(calculator.add(-3, -4), -7)

	def test_subtract(self):
		self.assertEqual(calculator.subtract(3, 4), -1)
		self.assertEqual(calculator.subtract(3, -4), 7)
		self.assertEqual(calculator.subtract(-3, -4), 1)

	def test_multiply(self):
		self.assertEqual(calculator.multiply(1, 10), 10)
		self.assertEqual(calculator.multiply(1, -10), -10)
		self.assertEqual(calculator.multiply(1+1j, 1+1j), 2j)

	def test_divide(self):
		self.assertEqual(calculator.divide(1, 10), 0.1)
		self.assertEqual(calculator.divide(1, -10), -0.1)
		self.assertEqual(calculator.divide(1+1j, 1+1j), 1)
		self.assertRaises(ValueError, calculator.divide, 1, 0)

	def test_power(self):
		self.assertEqual(calculator.power(4, 2), 16)
		self.assertEqual(calculator.power(4, 0), 1)
		self.assertEqual(calculator.power(4, -2), 1/16)
		self.assertEqual(calculator.power(4, 0.5), 2)


if __name__ == '__main__':
	unittest.main()