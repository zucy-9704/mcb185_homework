# 47cdsfinder.py	by Zucy

import sys
import sequence
import mcb185

s = sys.argv[1]

def cdsfinder(seq):
	seqs = seq.split('ATG')
	seqs.pop(0)
	for orf in seqs:
		aa = sequence.translate(orf)
		print('M', end = '')
		print(aa)

print(cdsfinder(s))
print(cdsfinder(sequence.revcomp(s)))