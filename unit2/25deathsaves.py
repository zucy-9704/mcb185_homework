# deathsaves.py	by Zucy

import random

health = 0
n = 99
pd = 0
ps = 0
pr = 0

for rounds in range(n):
	while True:
		d20 = random.randint(1, 20)
		if d20 == 1: health -= 2
		elif d20 == 20: 
			pr += 1
			print('You are revived!')
			health = 0
			break
		elif d20 >= 10: health += 1
		elif d20 < 10: health -= 1
		if health == 3: 
			ps += 1
			print('You are stable but unconscious')
			health = 0
			break
		if health <= -3: 
			pd += 1
			print('You died!! :(')
			health = 0
			break
	
print('Probability one dies, stabilizes, or revives:')
print('Dying:', pd/n)
print('Stabilizing:', ps/n)
print('Reviving:', pr/n)
