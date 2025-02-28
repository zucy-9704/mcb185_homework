# pairwisecomp.py	by Zucy

list = ['A', 'C', 'G', 'T']

# can compare elements on the list like:
	# all combinations
	# half matrix + diagonal (upper and lower)
	# half matrix w/o diagonal (upper and lower)
	
for i in range(0, len(list)):
	for j in range(i, len(list)):
		# X = 0 for all combinations
		# X = i for half matrix with diagonal
		# X = i + 1 for half matrix w/o diagonal
		print(f'Comparing {list[i]} and {list[j]}')