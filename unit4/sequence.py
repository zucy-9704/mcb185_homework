# sequence.py	by Zucy

def transcribe(dna):	# assuming you input the coding strand
	return dna.replace('T', 'U')	
	
def revcomp(dna):	
	rc = []	# need to make new list bc strings are immutable
	for nt in dna[::-1]:	# flip dna reverse (reverse loop)
		if nt == 'A': rc.append('T')	# dna complements
		elif nt == 'C': rc.append('G')
		elif nt == 'G': rc.append('C')
		elif nt == 'T': rc.append('A')
		else: rc.append('N')
	return ''.join(rc)	# join the list into a continuous string
	
def translate(dna):
	aas = []	# creates empty aa chain
	for i in range(0, len(dna), 3):	# every 3 nt is a new codon
		codon = dna[i:i+3]	# defines nt included in a codon
		if codon == 'ATG': aas.append('M')	# methionine
		elif codon == 'TAA': aas.append('*')	# lines 21-23 are stop codons
		elif codon == 'TAG': aas.append('*')
		elif codon == 'TGA': aas.append('*')
		else: aas.append('X')	# to continue, just define every other aa
	return ''.join(aas)	# return a string of aa (pp chain)
	
"""
# alternative way to write translate fxn
def translate(dna):
	codons = ('ATG', 'TAA', 'TAG', 'TGA')	# possible codons
	aminos = 'M***'	# index correlates w codons tuple
	aas = []	# populate this list to make aa seq
	for i in range(0, len(dna), 3):	# every three nt, start new codon
		codon = dna[i:i+3]	# one codon is three nt
		if codon in codons:	# if codon is in codon tuple
			idx = codons.index(codon)	# pull out index of matching codon
			aa = aminos[idx]	# match codon index to aa
			aas.append(aa)	# add this aa to aa list
		else:
			aas.append('X')	# anything that doesn't match codon on list will be X
	return ''.join(aas)	# return aa seq in string
"""

def gc_comp(seq):
	return((seq.count('C') + seq.count('G'))/len(seq))
	
def gc_skew(seq):
	c = seq.count('C')
	g = seq.count('G')
	if c + g == 0: return 0
	return (g - c)/(g + c)