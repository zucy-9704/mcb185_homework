# 51countgff.py	by Zucy

# similar to back in unit 0 when we counted all features in GFF
	# gunzip -c ecoli.gff.gz | grep -v "^#" | cut -f 3 | sort | uniq -c | sort -nr

import gzip
import sys

count = {}
	# create dictionary where key is the feature type and value is the number of times this feature type is counted
with gzip.open(sys.argv[1], 'rt') as fp:
	 for line in fp:
	 	if line.startswith('#'): continue	
	 		# this line skips all comments
	 		# skip to next line in fp
	 		# if this were pass, it would have no code associated with this conditional and go to next conditional
	 	f = line.split()
	 	feature = f[2]
	 	if feature not in count: count[feature] = 0
	 		# this is to add it to dictionary (add new key)
	 	count[feature] += 1
	 		# this increases count w ea occurrance
""" alternatively...
		if feature not in count: count[feature] = 1
		else: count[feature] += 1
"""
for f, n in count.items(): print(f, n)
	# count.items() separates k & v, making them iterable
print()
for k in sorted(count): print(k, count[k])
	
"""
sort dictionary by keys or values in CLI
1. python3 51countgff.py ecoli.gff.gz | sort
	- sort output by feature name
2. python3 51countgff.py ecoli.gff.gz | sort -n -k 2
	- sort output second column (-k 2) numerically (-n)
3. python3 51countgff.py ecoli.gff.gz | sort -nk2
	- collapsed version of #2
	
sort dictionary by keys in Python
for k in sorted(count): print(k, count[k])
"""