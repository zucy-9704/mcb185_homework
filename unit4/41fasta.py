# 41fasta.py	 by Zucy
import gzip
import mcb185
	# need to move this shortcut into whatever dir i am using it in
import sys

"""
with gzip.open(sys.argv[1], 'rt') as fp:
	for line in fp:
		print(line, end = '')
"""

for defline, seq in mcb185.read_fasta(sys.argv[1]):
	# defining two variables (defline & seq) in fasta file
	print(defline[:30], seq[:40], len(seq))
		# first 30 characters of defline
		# first 40 characters of seq
		# number of characters in seq
# ea record is returned as a tuple