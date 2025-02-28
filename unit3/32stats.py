# 32stats.py	by Zucy

import sys
import math

# number of values
numbers = []
for arg in sys.argv[1:]:
	float(arg)
	numbers.append(float(arg))
	
print(len(numbers))

# minimum and maximum values
def minmax(numbers):
	mini = numbers[0]
	maxi = numbers[0]
	for i in numbers:
		if i < mini: mini = i
		if i > maxi: maxi = i
	return mini, maxi

print(minmax(numbers))

# mean and std dev of values
def mean_stddev(numbers):
	tot = 0
	for i in numbers: tot += i
	mean = tot/(len(numbers))
	terms = []
	tot2 = 0
	for i in numbers: 
		terms.append((i - mean)**2)
		for vals in terms: tot2 += vals
	stddev = math.sqrt(tot2/(len(numbers) - 1))
	return mean, stddev
	
print(mean_stddev(numbers))
	
# median value
def median(numbers):
	numbers.sort()
	position = round(len(numbers)/2, 1)
	if position % 1 == 0: return numbers[int(position)]
	else: return (numbers[int(position + 0.5)] + numbers[int(position - 0.5)])/2

print(median(numbers))



