# 24savingthrows.py	by Zucy

import random

n = 50
p5 = 0
p5a = 0
p5d = 0
p10 = 0
p10a = 0
p10d = 0
p15 = 0
p15a = 0
p15d = 0

for rolls in range(n):
	d20 = random.randint(1,20)
	if d20 >= 15: 
		p15 += 1
		print('DC15 success')
	if d20 >= 10: 
		p10 += 1
		print('DC10 success')
	if d20 >= 5: 
		p5 += 1
		print('DC5 success')
	else: print('you failed :(')
	
for doubroll in range(n):
	d20i = random.randint(1,20)
	d20ii = random.randint(1, 20)
	if d20i > d20ii:
		if d20i >= 15: p15a += 1
		if d20i >= 10: p10a += 1
		if d20i >= 5: p5a += 1
		if d20ii >= 15: p15d += 1
		if d20ii >= 10: p10d += 1
		if d20ii >= 5: p5d += 1
	elif d20i < d20ii:
		if d20i >= 15: p15d += 1
		if d20i >= 10: p10d += 1
		if d20i >= 5: p5d += 1
		if d20ii >= 15: p15a += 1
		if d20ii >= 10: p10a += 1
		if d20ii >= 5: p5a += 1
	else: 
		if d20i >= 15: 
			p15d += 1
			p15a += 1
		if d20i >= 10: 
			p10a += 1
			p10d += 1
		if d20i >= 5: 
			p5d += 1
			p5a += 1
	
print('Probability of success under normal conditions:')
print('DC15:', p15/n)
print('DC10:', (p10)/n)
print('DC5:', (p5)/n)

print('Probability of success at an advantage:')
print('DC15:', p15a/n)
print('DC10:', (p10a)/n)
print('DC5:', (p5a)/n)

print('Probability of success at a disadvantage:')
print('DC15:', p15d/n)
print('DC10:', (p10d)/n)
print('DC5:', (p5d)/n)