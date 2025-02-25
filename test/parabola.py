# parabola.py	by Zucy

import random

x = 0
y = 0
above = 1
below = 1

while True:
	x = random.random()
	y = random.random()
	if y >= x**1:
		above += 1
	else: below += 1
	above_parabola = (above/below)
	print(above_parabola)