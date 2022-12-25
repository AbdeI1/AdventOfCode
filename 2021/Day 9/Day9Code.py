def reader():
	f = open("Day9input.txt", 'r').read()
	f = f.split('\n')
	f = f[:-1]
	return f

def getM(f, i, j):
	if i == -1 or i == 100 or j == -1 or j == 100:
		return 100
	return int(f[i][j])

def part1():
	f = reader()
	s = 0
	for i in range(100):
		for j in range(100):
			h = int(f[i][j])
			if h < getM(f, i-1,j) and h < getM(f, i+1, j) and h < getM(f, i,j-1) and h < getM(f, i,j+1):
				s += h+1
	print(s)

l = set()

def getBasinSize(f, i, j):
	if i == -1 or i == 100 or j == -1 or j == 100:
		return 0
	h = int(f[i][j])
	if (i,j) in l or h == 9:
		return 0
	l.add((i,j))
	return 1 + getBasinSize(f, i+1, j) + getBasinSize(f, i-1,j) + getBasinSize(f,i,j-1) + getBasinSize(f,i, j+1)

def part2():
	f = reader()
	basins = []
	for i in range(100):
		for j in range(100):
			h = int(f[i][j])
			if h < getM(f, i-1,j) and h < getM(f, i+1, j) and h < getM(f, i,j-1) and h < getM(f, i,j+1):
				basins.append(getBasinSize(f, i, j))
	basins.sort()
	print(basins[-1]*basins[-2]*basins[-3])

part1()
part2()
