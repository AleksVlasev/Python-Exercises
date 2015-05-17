__author__ = 'Vlasev'

# In this file we'll take a look at rational integers.
# Rational integers can be represented by pairs of numbers (a, b)
# for which we have some rules for addition and so on.


def gcd(a, b):
	while b:
		a, b = b, a % b
	return a

def reduce(a, b):
	a, b = a/gcd(a, b), b/gcd(a, b)
	return int(a), int(b)

def print_test(a, b):
	c = RationalNumber(a, b).get_printable()
	print("Inputting {} and {} leads to {}".format(a, b, c))

def add_rational(a, b):
	num = a.numerator * b.denominator + b.numerator * a.denominator
	den = a.denominator * b.denominator
	return RationalNumber(num, den)



class RationalNumber(object):
	# Need to add a check that denominator is not zero
	def __init__(self, numerator, denominator):
		self.numerator, self.denominator = reduce(numerator, denominator)
		# If we wish to not even work with zero denominators we may use
		# assert self.denominator != 0, "Looks like you are dividing by zero"

	def get_number(self):
		return [self.numerator, self.denominator]

	def get_printable(self):
		if self.denominator == 1:
			return str(self.numerator)
		elif self.denominator == 0:
			return "UND"
		else:
			return "{}/{}".format(self.numerator, self.denominator)

print()
print("Here we'll test some inputs and see if we get what we would expect\n")
# print_test(5, 10)
# print_test(-3, 6)
# print_test(7, 4)
# print_test(7, -1)
# print_test(0, 6)
# print_test(6, 0)

# numA = RationalNumber(3, 5)
# numB = RationalNumber(8, 0)
# numC = add_rational(numA, numB)
# print(numC.get_printable())


