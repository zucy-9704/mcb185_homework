# 40cdslength.py	by Zucy

import gzip
import sys

"""	# print all of gzipped file
with gzip.open('/Users/azucenavirgen/Code/MCB185/data/GCF_000005845.2_ASM584v2_genomic.gff.gz', 'rt') as fp:
	for line in fp:
		print(line, end = '')
"""

with gzip.open(sys.argv[1], 'rt') as fp:
	for line in fp: 
		if line[0] == '#': continue
		words = line.split()
		if words[2] == 'CDS':
			beg = int(words[3])
			end = int(words[4])
			print(end - beg + 1)

"""
with gzip.open(sys.argv[1], 'rt') as fp:
	for line in fp:
		if line[0] == '#': continue
			# if the line starts w '#', ignore the rest of the commands (continue)
			# continue is like a filter, filters out stuff in the if statement
		words = line.split()
		if words[2] != 'CDS': continue
			# filtering out lines that DON'T contain 'CDS'
		beg = int(words[3])
		end = int(words[4])
		print(end - beg + 1)
		

# need to type file path as argument after .py file name
with gzip.open(sys.argv[1], 'rt') as fp:
	for line in fp:	# defines ea line as part of a tuple
		if line[0] != '#':	# skip ('!=' means 'not equal to') over comment lines
			# you are indexing ea character in a line
			words = line.split()
				# split the words in ea line into strings, delimiter = [spaces]
				# makes list of strings (words)
			if words[2] == 'CDS':
				# [2] is position of DNA 'type'
				beg = int(words[3])	# define beginning
				end = int(words[4])	# define end
				# convert coordinates --> int
				print(end - beg + 1)	# calc length
"""				
				
				
				
				