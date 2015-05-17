__author__ = 'Vlasev'

# In this project we'll get to work with arbitrarily long integers with
# some naive methods. It's just a first project to see how things work


def to_number(string):
	result = []
	for s in string:
		result.append(s)
	return result



class BigIntegers(object):
	"""This class"""
	number = []

	def __init__(self, string):
		self.string = string
		self.number = to_number(string)

	def number_print(self):
		print(self.string)

	def get_number(self):
		return self.number


numb = BigIntegers(input("Enter a big integer: "))
numb.number_print()
