# 11oligo.py by Zucy

def tm(A, T, C, G):
	if A + T + C + G <= 13: return (A + T)*2 + (G + C)*4
	else: return 64.9 + 41*(G + C - 16.4)/(A + T + G + C)
	
print(tm(4, 5, 2, 8))
print(tm(38, 29, 48, 23))