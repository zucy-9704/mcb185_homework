# isprime.py	by Zucy

def isprime(i):
	for int in range(2, i):
		if (i / int) % 1 == 0: return False
	return True

print(isprime(3))
print(isprime(4))
		