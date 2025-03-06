# 44skew.py	by Zucy

import mcb185
import sequence
import sys

w = int(sys.argv[2])	# window is 10 characters long
g = 0
c = 0

for defline, seq in mcb185.read_fasta(sys.argv[1]):
	g = seq[0:w].count('G')
	c = seq[0:w].count('C')
	print(sequence.gc_comp(seq[0:w]), sequence.gc_skew(seq[0:w]))		
	for i in range(len(seq) - w - 1):	# i is number of open windows
		if seq[i] == 'G':
			g -= 1
		if seq[i] == 'C':
			c -= 1
		if seq[i+w+1] == 'G':
			g += 1
		if seq[i+w+1] == 'C':
			c += 1
		gc_comp = (g + c) / w
		if g + c == 0: skew = 0
		else: skew = (g - c)/(g + c)
		print(i, gc_comp, skew)