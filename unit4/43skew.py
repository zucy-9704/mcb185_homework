# 43skew.py	by Zucy

# program using a sliding window algorithm to compute
	# GC composition & 
	# GC-skew
	
import sequence

seq = 'ACGTACGTGGGGACGTACGTCCCCC'
w = 10	# window is 10 characters long
for i in range(len(seq) - w + 1):	# i is number of open windows
	s = seq[i:i+w]	# substring for ea window
	print(i, sequence.gc_comp(s), sequence.gc_skew(s))