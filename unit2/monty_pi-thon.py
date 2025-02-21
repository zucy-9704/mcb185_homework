# monty_pi-thon	by Zucy

import random

x = 0	#set initial value for x and y
y = 0
inside = 0	# set initial value for # points (inside & tot)
tot = 0

# incrementing can be used to COUNT NUMBER OF LOOPS #

while True:	# infinite loop
	tot += 1	# add one for every loop to count total points
	x = random.random()	# generate random #s for x and y (change w every loop)
	y = random.random()
	if x**2 + y**2 <= 1:	# calculate hypotenuse (sqrt not needed bc comparing to 1)
		inside += 1	# only points inside are incremented
	pi_est = 4 * inside / tot
	print(pi_est)	# bc working w 'while', cannot use 'return' fxn
