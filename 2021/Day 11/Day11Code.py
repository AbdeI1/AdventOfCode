def reader():
	f = open("Day11input.txt", 'r').read()
	f = f.split('\n')
	f = f[:-1]
	return f

def getM(m, i, j):
	if i == -1 or i == 10 or j == -1 or j == 10:
		return -1
	else:
		return m[i][j]

count = 0

def flash(m, i, j):
	global count
	count += 1
	m[i][j] = -1
	for c in range(-1,2):
		for b in range(-1,2):
			if not (c == 0 and b == 0):
				if getM(m, i+c, j+b) != -1:
					m[i+c][j+b] += 1

def simulate(o):
	for i in range(10):
		for j in range(10):
			o[i][j] += 1
	for k in range(100):
		for i in range(10):
			for j in range(10):
				if o[i][j] > 9:
					flash(o, i, j)
	for i in range(10):
		for j in range(10):
			if o[i][j] == -1:
				o[i][j] = 0

def part1():
	global count
	count = 0
	f = reader()
	o = [list(map(int,f[i])) for i in range(len(f))]
	for i in range(100):
		simulate(o)
	print(count)

def part2():
	global count
	count = 0
	f = reader()
	o = [list(map(int,f[i])) for i in range(len(f))]
	i = 0
	while True:
		l = count
		simulate(o)
		i += 1
		if count >= l + 100:
			break
	print(i)

part1()
part2()
