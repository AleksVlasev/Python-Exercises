__author__ = 'Vlasev'

# In this file we'll take a look at rational integers.
# Rational integers can be represented by pairs of numbers (a, b)
# for which we have some rules for addition and so on.


# This is the usual gcd function. I've included it like this for completeness
def gcd(a, b):
	while b:
		a, b = b, a % b
	return a


# If a, b are integers to begin with we are guaranteed that
# the outputs will be integers too.
def reduce(a, b):
	a, b = a/gcd(a, b), b/gcd(a, b)
	return int(a), int(b)


# Just a little helper to shows that the class works as advertised
def print_test(a, b):
	c = RationalNumber(a, b).get_printable()
	print("Inputting {} and {} leads to {}".format(a, b, c))


# Here are some binary operations on rational numbers
def multiply_rationals(a, b):
	num = a.numerator * b.numerator
	den = a.denominator * b.denominator
	return RationalNumber(num, den)


def divide_rationals(a, b):
	return multiply_rationals(a, b.get_multiplicative_inverse())


def add_rationals(a, b):
	num = a.numerator * b.denominator + b.numerator * a.denominator
	den = a.denominator * b.denominator
	return RationalNumber(num, den)


def subtract_rationals(a, b):
	return add_rationals(a, b.get_additive_inverse())


# Here is the class that keeps the rational numbers x/y as an object with two parameters x and y
# It automatically reduces the fraction
class RationalNumber(object):

	def __init__(self, numerator, denominator):
		self.numerator, self.denominator = reduce(numerator, denominator)
		# If we wish to not even work with zero denominators we may use
		# assert self.denominator != 0, "Looks like you are dividing by zero"

	def get_number(self):
		return [self.numerator, self.denominator]

	# For now we allow zero denominators, in which case we print UND for the fraction

	def get_printable(self):
		if self.denominator == 1:
			return str(self.numerator)
		elif self.denominator == 0:
			return "UND"
		else:
			return "{}/{}".format(self.numerator, self.denominator)

	def get_multiplicative_inverse(self):
		return RationalNumber(self.denominator, self.numerator)

	def get_additive_inverse(self):
		return RationalNumber(-self.numerator, self.denominator)

	def power(self, number):
		return RationalNumber(self.numerator ** number, self.denominator ** number)

	def absolute(self):
		return RationalNumber(abs(self.numerator), abs(self.denominator))


print()
print("Here we'll test some inputs and see if we get what we would expect\n")
# print_test(5, 10)
# print_test(-3, 6)
# print_test(7, 4)
# print_test(7, -1)
# print_test(0, 6)
# print_test(6, 0)

numA = RationalNumber(3, 5)
numB = RationalNumber(8, -3)
numC = add_rationals(numA, numB)
numD = numA.power(2)
print(numD.get_printable())
