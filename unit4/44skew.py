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
		s = seq[i:i+w]
		if s[i] == 'G':
			g -= 1
		if s[i] == 'C':
			c -= 1
		if s[i+w+1] == 'G':
			g += 1
		if s[i+w+1] == 'C':
			c += 1
		print((g + c)/w, (g - c)/(g + c))
			