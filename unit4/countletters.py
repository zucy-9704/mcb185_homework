# countletters.py	by Zucy

import sys
import mcb185

# instead of initializing for every letter, make a list and append ea new letter
nts = []
counts = []

# ea nt percentage
for defline, seq in mcb185.read_fasta(sys.argv[1]):
	defwords = defline.split()
	name = defwords[0]
	for nt in seq:
		if nt not in nts:
			nts.append(nt)	# add new letter
			counts.append(0)	# make list longer
		idx = nts.index(nt)
		counts[idx] += 1
	print(name)
	for nt, n in zip(nts, counts):	
		print(nt, n, n/len(seq))	# nt, counts, proportion
print()