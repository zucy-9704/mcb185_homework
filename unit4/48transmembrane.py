# 48transmembrane.py	by Zucy

import sys
import mcb185
import sequence

def hydrophobicity(seq):
	aas = 'IVLFCMAGTSWYPHEQDNKR'
	kds = [4.5, 4.2, 3.8, 2.8, 2.5, 1.9, 1.8, -0.4, -0.7, -0.8, -0.9, -1.3, -1.6, -3.2, -3.5, -3.5, -3.5, -3.5, -3.9, -4.5]
	kds_vals = []
	
	for aa in seq:
		kds_vals.append(kds[aas.index(aa)])
	return kds_vals

def tot(kds_vals):
	tot = 0
	for kds_val in kds_vals:
		tot += kds_val
	return tot

def is_transmem(seq):
	sigpep_region = seq[:30]
	transmem_region = seq[30:]
	stat1 = False
	stat2 = False
	for i in range(len(sigpep_region) - 8 + 1):
		sigpep = sigpep_region[i:i+8]
		average_sigpep_kd = tot(hydrophobicity(sigpep)) / 8
		
		if average_sigpep_kd >= 2.5 and 'P' not in sigpep:
			stat1 = True
			break
	for i in range(len(transmem_region) - 11 + 1):
		transmem = transmem_region[i:i+11]
		average_transmem_kd = tot(hydrophobicity(transmem)) / 11
		if average_transmem_kd >= 2 and 'P' not in transmem:
			stat2 = True
			break
	if stat1 and stat2: return True
	else: return False
	
for defline, seq in mcb185.read_fasta(sys.argv[1]):
	if is_transmem(seq):
		print(defline[:60])
	
	
	
	
	
	
	
