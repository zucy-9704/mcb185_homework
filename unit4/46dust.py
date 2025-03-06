# dust.py by Zucy

# shannon entropy: measurement of information in a system
	# shannon uses log base two
	# p(x) = # of nt in window / window size
	

import mcb185
import sys
import math

w = int(sys.argv[2])	# window is 20 characters long
ent_thresh = float(sys.argv[3])	# entropy threshold is 1.4

for defline, seq in mcb185.read_fasta(sys.argv[1]):
	for nt in seq:
		for nt in range(len(seq) - w + 1):
			s = seq[nt:nt+w]
			a = s.count('A')
			c = s.count('C')
			g = s.count('G')
			t = s.count('T')
			nts = a, c, g, t
			for i in nts:
				hlist = []
				if i == 0: continue
				p = i/w
				h = p * math.log2(p)
				hlist.append(h)
			H = -1 * math.fsum(hlist)
			if H < ent_thresh:
				newseq = seq.replace(seq[nt], 'N')
			print(newseq)


