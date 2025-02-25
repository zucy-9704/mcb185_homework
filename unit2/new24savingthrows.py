# new24savingthrows.py

import random

def minmax(r1, r2):
	if r1 > r2:
		maxi = r1
		mini = r2
	else: 
		maxi = r2
		mini = r1
	return maxi, mini

num_roll = 10000

for dc in range(5, 16, 5):
	normsuccess = 0
	highsuccess = 0
	lowsuccess = 0
	for i in range(num_roll):
		d20i = random.randint(1,20)
		d20ii = random.randint(1,20)
		normroll = d20i
		highroll, lowroll = minmax(d20i, d20ii)
		if normroll >= dc:
			normsuccess += 1
		if highroll >= dc:
			highsuccess += 1
		if lowroll >= dc:
			lowsuccess += 1
	print('DC:', dc)
	print('norm prob:', normsuccess/num_roll)
	print('disadvantage prob:', lowsuccess/num_roll)
	print('advantage prob:', highsuccess/num_roll)
		
