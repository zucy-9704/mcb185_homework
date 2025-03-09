#	kmerexample.py

import random
import time

def random_names(n, k):
	klist = list()	# generate empty list
	kset = set()	# generate empty set
	for _ in range(n):
		kmer = ''.join(random.choices('ACGT', k=k))
			# gen random choices of nts, length k
		klist.append(kmer)	# adding them to list will add all
		kset.add(kmer)	# adding them to set will only add unique seqs
	return klist, kset

for size in range(1000, 10000, 1000):
	# 1000, 2000, 3000, ..., 8000, 9000
	list1, set1 = random_names(size, 10)
	list2, set2 = random_names(size, 10)

	t0 = time.time()
	for name1 in list1:
		if name1 in list2: pass	# no code is associated with pass
	t1 = time.time()
	list_time = t1 - t0
		# time for program to run the iteration

	t0 = time.time()
	for name1 in list1:
		if name1 in set2: pass
	t1 = time.time()
	set_time = t1 - t0
		# this time is going to be faster because sets only have unique sequences

	print(list_time, set_time, list_time/set_time)