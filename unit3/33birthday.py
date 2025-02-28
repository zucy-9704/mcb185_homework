# 33birthday.py	by Zucy

import random
import sys

trials = int(sys.argv[1])
days = int(sys.argv[2])
people = int(sys.argv[3])
success = 0

for i in range(trials):
	bdays = []
	print('trial #', i)
	for j in range(people):
		k = random.randint(0, 365)
		if k in bdays: 
			success += 1
			break
		else: bdays.append(k)
		print(bdays)
print(success/trials)


