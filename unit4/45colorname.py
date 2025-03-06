# 45colorname.py	by Zucy

import sys

colorfile = sys.argv[1]
R = int(sys.argv[2])
G = int(sys.argv[3])
B = int(sys.argv[4])
minimum = 750
min_color = 'none'

with open(colorfile, 'rt') as fp:
	for line in fp:
		colorprofile = line.split()	
		colorvalues = colorprofile[2].split(',')		
		diff1 = abs(int(colorvalues[0]) - R)
		diff2 = abs(int(colorvalues[1]) - G)
		diff3 = abs(int(colorvalues[2]) - B)
		sum = diff1 + diff2 + diff3
		if sum < minimum: 
			minimum = sum
			min_color = colorprofile[0]
	print(min_color)
	
