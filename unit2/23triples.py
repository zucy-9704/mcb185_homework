# 23triples.py by Zucy
"""
import random
import math

a = 0
b = 0

while True:	# this is an infinite loop
	a = random.randint(1, 100)
	b = random.randint(1, 100)
	c = math.sqrt(a**2 + b**2)
	if c % 1 == 0: print(a, b, c)
"""

import math
import random
"""
a = 0	#lines 19 & 20 not necessary bc we are not storing these values
b = 0
"""
n = 100
# a 'for' loop results in a finite list
for a in range(1, n):	# defining length of side a
	for b in range(a, n):	# length of side b depends on length of side a
		c = math.sqrt(a**2 + b**2)	# calculating length of side c
		if c % 1 == 0: print(a, b, c)	# test if c is an integer