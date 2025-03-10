# 53dust.py	Zucy

import argparse	# import library

# input: file, size, and entropy
# for more info on what to input, add -h flag

# positional arguments rely on input's position in command line
parser = argparse.ArgumentParser(description = 'DNA entropy filter.')
	# create argument parser object in a variable called 'parser'
parser.add_argument('file', type = str, help = 'name of fasta file')
	# adds positional argument for path to a FASTA file
parser.add_argument('-s', '--size', type = int, default = 20, help = 'window size [%(default)i]')
	# adds positional argument for window size and specifies int value
	# advertise default value w %(default)
	# append w s, i, or f to indicate string, integer, or float
parser.add_argument('-e', '--entropy', type = float, default = 1.4, help = 'entropy threshold [%(default).3f]')
	# adds positional argument for entropy threshold and specifies float value
	# advertise default value
	# .3f is three digits of precision
parser.add_argument('--lower', action = 'store_true', help = 'soft mask')
	# in analyzing low-complexity regions, changes low-complexity regions to lowercase letters instead
	# basically like on/off switch for soft-masking low-complexity regions
arg = parser.parse_args()
	# arg variable harvests values on command line
print('dusting with', arg.file, arg.size, arg.entropy, arg.lower)

# to override window size & entropy:
# python3 53dust.py e.coli.fa.gz --size 15 --entropy 1.2




