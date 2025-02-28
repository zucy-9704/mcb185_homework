# 35scoringmatrix.py	by Zucy

import sys

nts = sys.argv[1]
matches = sys.argv[2]
mismatches = sys.argv[3]

print('   ', end = '')

for nt in nts:
	print(nt, end = '  ')
print()

for nt1 in nts:
	print(nt1, end = ' ')
	for nt2 in nts:
		if nt1 == nt2: print(matches, end = ' ')
		else: print(mismatches, end =' ')
	print()
