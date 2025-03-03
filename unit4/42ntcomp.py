# 42ntcomp.py	by Zucy

import sys
import mcb185

# counting with str.count()
for defline, seq in mcb185.read_fasta(sys.argv[1]):
	defwords = defline.split()
	name = defwords[0]
	print(name, end = ' ')
	for nt in 'ACGTN':
		print(seq.count(nt)/len(seq), end = ' ')
	print()

"""
# Counting letters in a list
nts = []
counts = []

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

# indexing w str.find()
for defline, seq in mcb185.read_fasta(sys.argv[1]):
	defwords = defline.split()
	name = defwords[0]
	nts = 'ACGTN'	# make list of desired nts
	counts = [0] * len(nts)	# make list of 0's as long as nts list
	for nt in seq:
		idx = nts.find(nt)
		# everytime the desired nt comes up, link index in nts list to index in counts list
		counts[idx] += 1
		# index in nts & counts are same
	print(name, end = ' ')
	for n in counts: print(n/len(seq), end = ' ')
	print()

# more efficient way to print proportions
for defline, seq in mcb185.read_fasta(sys.argv[1]):
	defwords = defline.split()
	name = defwords[0]
	counts = [0, 0, 0, 0, 0]	# A, C, G, T, N
	for nt in seq:
		if nt == 'A': counts[0] += 1
		elif nt == 'C': counts[1] += 1
		elif nt == 'G': counts[2] += 1
		elif nt == 'T': counts[3] += 1
		else: counts[4] += 1
	print(name, end = ' ')
	for n in counts: print (n/len(seq), end = ' ')
	print()

# does the same as code above
for defline, seq in mcb185.read_fasta(sys.argv[1]):
	defwords = defline.split()
	name = defwords[0]
	A = 0
	C = 0
	G = 0
	T = 0
	N = 0
	for nt in seq: 
		if nt == 'A': A =+ 1
		elif nt == 'C': C += 1
		elif nt == 'G': G += 1
		elif nt == 'T': T += 1
		else: N += 1
	print(name, A/len(seq), C/len(seq), G/len(seq), T/len(seq), N/len(seq))

# gc content in the seq
for defline, seq in mcb185.read_fasta(sys.argv[1]):
	# variables defline and seq
	defwords = defline.split()
		# separate defline into list of strings
	name = defwords[0]
		# select first string of defline list
	gc = 0
	for nt in seq:
		if nt == 'C' or nt == 'G': gc += 1
	print(name, gc/len(seq))
"""