# 47cdsfinder.py	by Zucy

import sys
import sequence
import mcb185

s = sys.argv[1]

def cdsfinder(fasta_file):
	for defline, seq in mcb185.read_fasta(fasta_file):
		seqs = seq.split('ATG')
		seqs.pop(0)
		for orf in seqs:
			aa = sequence.translate(orf)
			print('M', end = '')
			if aa[-1] == '*': print(aa)
			else: print(aa, end = '')

print(cdsfinder(s))
for defline, seq in mcb185.read_fasta(s):
	print(cdsfinder(sequence.revcomp(seq)))
