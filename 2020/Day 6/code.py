def part1():
	f = open("C:/Users/bluey/Documents/Coding Projects/AdventOfCode/Day 6/Day6input.txt", 'r').read()
	f = f.split('\n')
	a = []
	total = 0
	for s in f:
		if s == '':
			total += len(a)
			a = []
			continue
		i = 0
		while i < len(s):
			if not (s[i] in a):
				a.append(s[i])
			i += 1
	print(total)


def part2():
	f = open("C:/Users/bluey/Documents/Coding Projects/AdventOfCode/Day 6/Day6input.txt", 'r').read()
	f = f.split('\n')
	total = 0
	a = []
	for s in f:
		if s == '':
			i = 0
			first = a[0]
			while i < len(first):
				inAll = True
				for q in a:
					inAll = inAll and (first[i] in q)
				if inAll:
					total += 1
				i += 1
			a = []
			continue
		a.append(s)
	print(total)


part1()
part2()