def part1():
	f = open("C:/Users/bluey/Documents/Coding Projects/AdventOfCode/Day 10/Day10input.txt", 'r').read()
	f = f.split('\n')
	f = f[: len(f) - 1]
	i = 0
	while i < len(f):
		f[i] = int(f[i])
		i += 1
	f.append(0)
	f.append(max(f) + 3)
	f = sorted(f)
	i = 1
	oneJolts = 0
	threeJolts = 0
	while i < len(f):
		if f[i] - f[i - 1] == 1:
			oneJolts += 1
		elif f[i] - f[i - 1] == 3:
			threeJolts += 1
		i += 1
	print(f)
	print(oneJolts)
	print(threeJolts)
	print(oneJolts * threeJolts)


def reader():
	f = open("C:/Users/bluey/Documents/Coding Projects/AdventOfCode/Day 10/Day10input.txt", 'r').read()
	f = f.split('\n')
	f = f[: len(f) - 1]
	i = 0
	while i < len(f):
		f[i] = int(f[i])
		i += 1
	f.append(0)
	f.append(max(f) + 3)
	f = sorted(f)
	return f

a = [0] * 188

def part2():
	f = reader()
	print(f)
	i = len(f) - 1
	while i > -1:
		num = f[i]
		a[num] = newRecursion(num)
		i -= 1
	print(a)

f = reader()
#new recursive answer, takes much less time since answers are being stored in list
def newRecursion(x):
	if x not in f:
		return 0
	if x == 187:
		return 1
	if a[x] != 0:
		return a[x]
	return newRecursion(x + 1) + newRecursion(x + 2) + newRecursion(x + 3)




def howManyRemove(f):
	count = 0
	a = []
	i = 2
	while i < len(f):
		if f[i] - f[i - 2] <= 3:
			count += 1
			a.append(i - 1)
		i += 1
	return (count, a)

# Recursive answer, takes way too long, not even sure it works
def countRemove(f):
	h = howManyRemove(f)
	if h[0] == 0:
		return 0
	count = h[0]
	a = h[1]
	for i in a:
		e = f
		print(i)  #exists so I can know if code is running
		count += countRemove(e[0:i] + e[i + 1: len(e)])
	return count



part2()