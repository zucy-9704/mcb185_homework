# newphred by Zucy

import math

def char_to_prob(c):
	return 2**(47-ord(c))
	
print(char_to_prob('0'))
print(char_to_prob('9'))

def prob_to_char(x):
		return chr(int(-math.log2(x)) + 47)
		
print(prob_to_char(0.1))
print(prob_to_char(0.25))