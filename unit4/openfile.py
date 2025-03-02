# openfile.py	by Zucy

with open('/Users/azucenavirgen/Code/mcb185_homework/test/favorites.md', 'r') as fp:
	# make path understandable for unix environment
	for line in fp: 	# for every line in fp(file)
		print(line)	# print every line