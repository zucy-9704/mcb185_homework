# 10demo.py by Zucy

print ('hello, again') #greeting

print (1.5e-2)
print (4**0.5)

import math

print (math.pow(2, 3))

# solve for the hypotenuse of a triangle with sides 3 and 4
a = 3								#side of triangle
b = 4								#side of triangle
c = math.sqrt (a**2 + b**2)			#hypotenuse
print (c)
print (type(a), type(b), type(c), sep=', ', end='!\n')

def circ_area (r): return math.pi * r**2
print (circ_area(3))

def rect_area (w, h): return w * h
print (rect_area(3, 4))

# 'if' statements
a = 0.3
b = 4
if a==b: 
	print ('a equals b')
	print (a, b)
	
def is_even(x):
	if x % 2 == 0: 
		return True			#if x is evenly divisible by 2, return the statement True
	return False			#everything else, return the statement False

print(is_even(2))
print(is_even(3))

c = a == b
print (c)
print (type(c))

if a < b: print('a < b')
elif a > b: print('a > b')
else: print('a==b')

if math.isclose(a, b): print ('close enough')

s1 = 'A'
s2 = 'B'
s3 = 'a'
if s1 < s2: print ('A < B')
if s2 < s3: print ('B < a')

def silly(m, x, b): y = m * x + b
print(silly(2, 3, 4))
