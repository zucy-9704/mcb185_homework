# 31entropy.py	by Zucy

import math
import sys

probs = []	# create empty list
for arg in sys.argv[1:]:	# for all the command line arguments AFTER file name
	f = float(arg)	# turn all the arguments you can into floats
	if f <= 0 or f >= 1: sys.exit('error: not a probability')
		# customize error conditions and message
	probs.append(float(arg))
	
total = 0	# initialize total
for p in probs: total += p	# add all appended probs
if not math.isclose(total, 1.0):	# check if tot is close to 1.0
	# never ask if floating numbers are equal to anything
	sys.exit('error: probs must sum to 1.0')

h = 0	# Shannon entropy
for p in probs:	# calculating entropy (idk this eqn)
	h -= p * math.log2(p)
	
print(f'{h:.4f}')	# print entropy w 4 fixed digits after decimal
	# f-string










