__author__ = 'Vlasev'
'''Let's be honest here. The fizz-buzz exercise is nothing more than an exercise in listing
	all the prime divisors of a number, where instead of the factors we're printing fizz/buzz or a combination.
	Just for fun we'll implement a general procedure for highlighting if numbers in a list have specific prime factors'''

def fizz(num, k):
	'''This function just tests if num is divisible by k'''
	if num % k == 0:
		return True
	else:
		return False


def num_fizz(num, array):
	'''For a given number num and a collection of numbers in array, we iteratively build the label that we'll
	have for num.'''
	marked = False
	label = ""
	for a in array:
		marked = marked or fizz(num, a)
		if fizz(num, a) and len(label) == 0:
			label += ": {}".format(a)
		elif fizz(num, a) and len(label) > 0:
			label += ", {}".format(a)
	if marked:
		return "{} is divisible by ".format(num) + label
	else:
		return "{} is not divisible by any number in array.".format(num)


def full_fizz(low, high, array):
	print("\nThe numbers to test are {} - {} and the array is ".format(low, high) + str(array) + "\n")
	for num in range(low, high):
		print(num_fizz(num, array))

full_fizz(1, 101, [3, 5])  # Original Fizz-Buzz-like exercise
full_fizz(1, 201, [2, 3, 5, 7])  # Extending to more inputs
full_fizz(1, 201, [2, 6, 5, 10])  # They don't have to be prime numbers
