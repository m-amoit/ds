fhand = open('romeo.txt')
counts = dict()
for line in fhand:
	words = line.split()
	for word in words:
		counts[word] = counts.get(word, 0) + 1
	
print counts

# Sort dictionary by value

lst = list()
for k, v in counts.items():
	lst.append( (v, k))
print ''
lst.sort(reverse=True)

for k, v in lst[:10]:
	print v, k






input()