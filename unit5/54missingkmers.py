# 54missingkmers.py	by Zucy

import sys
import itertools
import mcb185
import sequence

# identify how many kmers there are for increasing k
	# stop loop at smallest k w/ missing kmers
	# report missing kmers
	# search both strands
	
for k in range(100):
	kcount = {}
	for defline, seq in mcb185.read_fasta(sys.argv[1]):
		rcseq = sequence.revcomp(seq)
		for i in range(len(seq) - k + 1):
			kmer1 = seq[i:i+k]
			kmer2 = rcseq[i:i+k]
			if kmer1 not in kcount: kcount[kmer1] = 0
			if kmer2 not in kcount: kcount[kmer2] = 0
			kcount[kmer1] += 1
			kcount[kmer2] += 1
	if 4**k > len(list(kcount.keys())):
		print('k is', k, 'and there are', (4**k) - len(list(kcount.keys())), 'missing kmers')
		for nts in itertools.product('ACGT', repeat = k):
			kmer = ''.join(nts)	
				# joins tuple nts into string to index dictionary
			if kmer in kcount: pass
			else: print(kmer, 0)
				# report any kmers that are not in kcount
		break
		
		
