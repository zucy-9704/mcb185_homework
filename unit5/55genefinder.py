# 55genefinder.py	by Zucy

# reports putative coding gene coordinates
	# input: FASTA file
	# output: GFF of gene features
	
import sys
import sequence
import mcb185


for defline, seq in mcb185.read_fasta(sys.argv[1]):
	rcseq = sequence.revcomp(seq)
	for frame in range(3):
		print()
		print('frame', frame)
		i = frame
		while i < len(seq):
			codon = seq[i:i+3]
			if codon != 'ATG':
				i += 3
				continue
			if codon == 'ATG':
				stop = None		# necessary line bc there is possibility for there to be no stop codon
				for j in range(i+3, len(seq), 3):
					codon = seq[j:j+3]
					if codon == 'TAA' or codon == 'TAG' or codon == 'TGA':
						stop = j + 2
						if stop - i >= 300:
							print('seq', end = '	')
							print('ATG', 'CDS start at', i, end = '	')
							print(codon, 'CDS end at', j+2)
							print()
						break
			if stop == None: break	# break while loop
			i = stop + 1
		i = frame
		while i < len(rcseq):
			rc_codon = rcseq[i:i+3]
			if rc_codon != 'ATG':
				i += 3
				continue
			if rc_codon == 'ATG':
				stop = None		# necessary line bc there is possibility for there to be no stop codon
				for j in range(i+3, len(rcseq), 3):
					rc_codon = rcseq[j:j+3]
					if rc_codon == 'TAA' or rc_codon == 'TAG' or rc_codon == 'TGA':
						stop = j + 2
						if stop - i >= 300:
							print('rcseq', end = '	')
							print('ATG', 'CDS start at', i, end = '	')
							print(rc_codon, 'CDS end at', j+2)
							print()
						break
			if stop == None: break	# break while loop
			i = stop + 1
				