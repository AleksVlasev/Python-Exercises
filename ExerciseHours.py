__author__ = 'Vlasev'
from datetime import datetime
import math

'''In this file we can see a simple menu with options that actually do things!
I wanted to implement an example of a dictionary even though it's not REALLY necessary
Similarly I wanted to try reading from or writing to a file'''

'''The structure of this example is as follows. We call a function menu() which takes us through the various options
each of which calls a different function which is a different menu. This makes it easy to go back and forth between
menus. I'm sure there are better approaches but this is what I whipped up for the example. There are a few math functions
involved here too.'''

'''First we have the main menu'''

menu_numbers = [1, 2, 3, 4]
menu_items = {"1": "Log Hours", "2": "Check Stats ", "3": "Settings (Not Yet)", "4": "Exit"}


def menu():
	good_answer = False
	while not good_answer:
		print("\nPlease choose one of the following options:")
		for item in menu_numbers:
			print("   {}. {}".format(item, menu_items[str(item)]))
		key = input("Choose: ")
		if key in menu_items:
			good_answer = True
			choice(key)
		else:
			print("Sorry, that is an invalid option. Please enter a number from 1 to 4")
			good_answer = False


def choice(key):
	if key == "1":
		log_hours()
	elif key == "2":
		stat_menu()
	elif key == "3":
		pass
	elif key == "4":
		pass


def log_hours():
	file = open("raw_data.txt", "a")
	now = datetime.today()
	hours = input("\nHow many hours did you train today? ")
	file.write("{}-{}-{}, {}\n".format(now.year, now.month, now.day, hours))
	print("\nThanks, that is {} hours recorded for {}-{}-{}!".format(hours, now.year, now.month, now.day))
	file.close()
	menu()

''' Here is the stats menu'''

stat_numbers = [1, 2, 3, 4, 5]
stat_items = {"1": "All", "2": "Total", "3": "Average", "4": "Standard Deviation", "5": "Back to top menu"}


def stat_menu():
	good_answer = False
	while not good_answer:
		print("\nPlease choose one of the following options:")
		for item in stat_numbers:
			print("   {}. {}".format(item, stat_items[str(item)]))
		key = input("Choose: ")
		if key in stat_items:
			good_answer = True
			stat_choice(key)
		else:
			print("Sorry, that is an invalid option. Please enter a number from 1 to 5")
			good_answer = False


def stat_choice(key):
	hours = import_hours()
	if key == "1":
		print("Total: {}, Average: {}, Standard Deviation: {}\n".format(total(hours), average(hours), stddev(hours)))
	elif key == "2":
		print("Total: {}".format(total(hours)))
	elif key == "3":
		print("Average: {}".format(average(hours)))
	elif key == "4":
		print("Standard Deviation: {}".format(stddev(hours)))
	elif key == "5":
		menu()

	if key != "5":
		stat_menu()


# Simply open a file, read it line by line, splitting the formatting to get the hours
def import_hours():
	hours = []
	with open("raw_data.txt", "r") as file:
		for line in file:
			hours.append(float(line.split(", ")[1]))
	return hours

'''Simple math functions'''

def total(numbers):
	result = 0
	for num in numbers:
		result += num
	return result


def average(numbers):
	return math.ceil(10 * float(total(numbers))/len(numbers))/10


def variance(numbers):
	avg = average(numbers)
	result = 0
	for num in numbers:
		result += (num - avg)**2
	return float(result)/len(numbers)


def stddev(numbers):
	temp = math.sqrt(variance(numbers))
	return math.ceil(temp * 10)/10


menu()
