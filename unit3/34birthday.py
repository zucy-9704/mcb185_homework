# 34birthday.py	by Zucy

import sys
import random

trials = int(sys.argv[1])
days = int(sys.argv[2])
ppl = int(sys.argv[3])
success = 0

for t in range(0, trials):
	# make calendar
	calendar = []
	for i in range(0, 365):	# making the calendar
		calendar.append(0)
		
	# fill calendar
	for j in range(0, ppl):
		calendar[random.randint(0, len(calendar)-1)] += 1
		
	# check for bday collisions
	sharedbdays = False
	for i in range(len(calendar)):
		if calendar[i] > 1: sharedbdays = True
	if sharedbdays: success += 1
	
print(success/trials)






