__author__ = 'Vlasev'

from math import pi
import random
import time

estimate = 0
times = 10**7
start = time.clock()
for k in range(0, times + 1):
	x = random.random()
	y = random.random()
	if x**2 + y**2 > 1:
		estimate += 1
end = time.clock()
print(4*(1-float(estimate)/times))
print("It took {} seconds".format(str(end-start)))

