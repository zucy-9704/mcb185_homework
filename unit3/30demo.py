# 30demo.py	by Zucy

import math

s1 = 'hey "dude"'
s2 = "don't 'tell' me what to do!!!"
print(s1, s2)

# backslash indicates it's not fr fr
print('hey "dude" don\'t tell me what to do okay?')

"""
function(string)  # function syntax
string.method()    # method syntax
"""

s = 'i love my lola cat'
print(s.upper())
print(s)
print(s.replace('o', ' '))
print(s.replace('o', ' ').replace('t', 'r'))

# f-string formatting
print(f'{math.pi}')	# prints pi
print(f'{math.pi:.3f}')	# 3fixed digits after the decimal
print(f'{1e6 * math.pi:e}')	# does the multiplication and formats answer into exponent form
print(f'{"hello world":>20}')	# prints string and does right justified 20 spaces
print(f'{"hello world":.>20}')	# prints string and right justifies with 20 dots
print(f'{20:<10} {10}')	# left justifies '20' 10 spaces away from '10'
print(f'{"BOO!":e^50}')	# center justifies string amid a bunch of e's

# str.format() formatting
print('{} {:.3f}'.format('str.format', math.pi))
	# {} fill in sequentially with variables inside the parentheses
#printf-style
print('%s %.3f' % ('printf', math.pi))
	# this statement has similar rules to that of str.format() formatting
	# sequential filling
	
# Indexes
seq = 'GAATTC'
print(seq[0], seq[1])	#prints first and second letters in sequence
print(seq[-1]) # prints last letter of the string

for nt in seq:	# does a loop through the letters in string seq
	print(nt, end = '*')	# adds * to the end of each nt
print()

for i in range(len(seq)):
	print(i, seq[i])	# prints nt index and nt itself

z = 'ABCDEFGHIJK'
print(z[0:5])	# [a:b] is a slice, so only first 5 letters are printed (5 is an end-before limit)
	# slices can have an increment too [a:b:c], like range
print(z[0:8:2])	# first to seventh letter, increments by every other letter
	# first value default is beginning of string
	# second value default is end of string
	# increment default is 1
	
print(z, z[::], z[::1], z[::-1])
	# [::a] determines order of how string is printed
	# [::1] prints in normal order
	# [::2] prints every other letter
	# [::-1] prints backwards
	# [::-2] prints backwards and every other letter
	
# slicing a string into indiv codons
dna = 'ATGCTGTAA'
for i in range(0, len(dna), 3):
	codon = dna[i:i+3]
	print(i, codon)

nts = 'ACGT'
for i, nt in enumerate(nts):
	print(i, nt)
print(list(enumerate(nts)))

names = ('adenine', 'cytosine', 'guanine', 'thymine')
for i in range(len(names)):
	print(nts[i], names[i])	# using two containers simultaneously
for nt, name in zip(nts, names):	#prints in different lines
	print(nt, name)
print(list(zip(nts, names)))	#prints all in one line

for i, (nt, name) in enumerate(zip(nts, names)):
	print(i, nt, name)

# lists: use sqr brackets and contents are mutable
nts = ['a', 'T', 'g']
print(nts)
nts[2] = 'g'	# changing the contents of the list
print(nts)
nts.append('C')	# add 'C' to end of nts list
	# append can only add one thing at a time
print(nts)
nts.pop()	# remove elements from the end of nts list
print(nts)
nts.sort()	# sort a list by ASCII number or numerically (int or float)
print(nts)
nts.sort(reverse = True)	# reverse = True reverses the order
print(nts)

# list copying
nucleotides = nts.copy()
nucleotides.append('poopy')	# this line adds poopy only to the 'nucleotides' list
print(nts, nucleotides)

# creating a list
thingies = list()	# list() w/o arguments creates empty list
stuff = []	# empty square brackets also make empty list
thingies.append('yarn')
stuff.append('tortoiseshell cat')
stuff.append(3)
print(thingies)
print(stuff)

letters = 'AJFURICNESKCLI'
print(letters)	# fxn prints whole chunk
aas = list(letters)	# putting it into a list separates ea letter
print(aas)

# str.split()
words = 'everything is				AWESOME'
print(words)
sayit = words.split()	#split fxn separates individual words
print(sayit)

	# if you want to split words based on another delimiter, specify it in the fxn
		# useful for TSV or CSV data
line = '1.42,25.64,2.45'
print(line.split(','))	# define delimiter as a comma

# join lists!!
	# define a new delimiter
s = '-'.join(aas)	# joins these random letters with a dash
print(s)
s = ' '.join(aas)	# joins random letters with a space
print(s)

# search for specific items in containers
	# in, find(), and index()
if 'A' in letters: print('yay!!')
if 'a' in letters: print('aur naurrr')

# print('index G?', letters.index('H'))	# if it can't find the matching item, you can an error message :()
print('index A?', letters.index('A'))
	# prints message & tells you location of substring

print('index G?', letters.find('G'))	# if it can't find substring, returns -1
print('index A?', letters.find('A'))
	# prints message & returns location of substring

# command line data must be converted to int and floats
i = int('42')
x = float('0.4579')
print(i * x)

# x = float('hi:3')	# cannot be converted into a float :(


import sys
print(sys.argv)	# sys.argv is a list















