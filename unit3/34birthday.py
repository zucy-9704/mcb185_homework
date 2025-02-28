# 34birthday.py	by Zucy

import sys
import random

trials = int(sys.argv[1])
ppl = int(sys.argv[2])

for i in range(0, 365):	# making the calendar
		calendar = []
		calendar.append(i)

for t in range(0, trials):
	for j in range(0, ppl):
		calendar[random.randint(0, len(calendar)-1)] += 1
		
print(calendar)