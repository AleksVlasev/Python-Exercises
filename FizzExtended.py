__author__ = 'Vlasev'

'''In this exercise we'll implement a Fizz-Buzz-like procedure for any input array of number conditions'''

def fizz(num, k):
	if num % k == 0:
		return True
	else:
		return False

def num_fizz(num, array):
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
		return "{} is not divisible by any numbers in array.".format(num)

def full_fizz(low, high, array):
	print("\nThe numbers to test are {} - {} and the array is ".format(low, high) + str(array) + "\n")
	for num in range(low, high):
		print(num_fizz(num, array))

full_fizz(1, 101, [2, 3, 5, 7])