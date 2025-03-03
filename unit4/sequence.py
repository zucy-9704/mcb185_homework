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
	return '',join(rc)	# join the list into a continuous string