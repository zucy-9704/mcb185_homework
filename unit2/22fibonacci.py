# 22fibonacci.py by Zucy

n0 = 0
n1 = 1

print(n0)
print(n1)
for i in range(4): 
	n0 = n1 + n0
	n1 = n1 + n0
	print(n0, n1)
	
n0 = 0
n1 = 1

print(n0)
print(n1)
for i in range(8):
	n2 = n0 + n1
	n0 = n1
	n1 = n2
	print(n2)