# 35scoringmatrix.py	by Zucy

import sys

nts = sys.argv[1]
matches = sys.argv[2]
mismatches = sys.argv[3]

print('   ', end = '')	# spacing in front of the header

for nt in nts:	# header
	print(nt, end = '  ')
print()	# inserts a newline character

for nt1 in nts:	# pairwise comparison
	print(nt1, end = ' ')
	for nt2 in nts:
		if nt1 == nt2: print(matches, end = ' ')
		else: print(mismatches, end =' ')
	print()
