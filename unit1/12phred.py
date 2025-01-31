#12phred.py by Zucy

import math

def char_to_prob(c):
	return 10**-(ord(c) - 33)
	
print(char_to_prob('A'))
print(char_to_prob('!'))

def prob_to_char(x):
	if 0.0 < x <= 1.0:
		return chr(round((-1 * math.log10(x)) + 33))
	else: return

print(prob_to_char(0.001))
print(prob_to_char(12))
