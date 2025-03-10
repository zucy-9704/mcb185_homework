# 52kmercount.py	by Zucy

# kmer: seq of length k (k is a small integer)
	# sub-seq in sliding window algorithms are kmers
	
import sys
import mcb185
import itertools
	
k = int(sys.argv[2])
kcount = {}	# create dictionary
	# key is kmer
	# value is number of occurrences
for defline, seq in mcb185.read_fasta(sys.argv[1]):
	for i in range(len(seq) - k + 1):
		kmer = seq[i:i+k]
		if kmer not in kcount: kcount[kmer] = 0
		kcount[kmer] += 1
for kmer, n in kcount.items(): print(kmer, n)

for nts in itertools.product('ACGT', repeat = k):
	kmer = ''.join(nts)	
		# joins tuple nts into string to index dictionary
	if kmer in kcount: print(kmer, kcount[kmer])
	else: print(kmer, 0)
		# report any kmers that are not in kcount
		
"""
to view which kmers are not in ecoli genome
python3 52kmercount.py ecoli.fa.gz 7 | sort -nk2 | head
	shows top 10 lines
"""		
		
		
		
		
		
		
		
		
		
		
		
		