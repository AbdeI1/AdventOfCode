def reader():
	f = open("Day16input.txt", 'r').read()
	f = f.split('\n')
	f = f[:-1]
	return f

su = 0

def parseLit(s,i):
	while i < len(s) and s[i] != '0':
		i += 5
	i += 5
	return i

def parseOpZ(s,i):
	length = int(s[i:(i+15)],2)
	i += 15
	end = i + length
	while i < end:
		i = parseOp(s, i)
	return i

def parseOpO(s,i):
	num = int(s[i:(i+11)],2)
	i += 11
	for _ in range(num):
		i = parseOp(s, i)
	return i

def parseOp(s, i):
	global su
	beg = i
	while i < len(s):
		if s[i] == '1':
			break
		i += 1
	if i >= len(s):
		return len(s)
	i = beg
	v = s[i:(i+3)]
	su += int(v, 2)
	i += 3
	t = s[i:(i+3)]
	i += 3
	if int(t,2) == 4:
		i = parseLit(s,i)
	else:
		if s[i] == '0':
			i = parseOpZ(s,i+1)
		else:
			i = parseOpO(s,i+1)
	return i


def part1():
	global su
	f = reader()
	h = int(f[0],16)
	start = (format(int(f[0][0],16),"#06b"))
	start = start[2:]
	ind = 0
	b = bin(h)
	s = b[2:]
	while start[ind] == '0':
		s = '0' + s
		ind += 1
	parseOp(s, 0)
	print(su)

def parseLit2(s,i):
	b = ""
	while i < len(s) and s[i] != '0':
		b += s[(i+1):(i+5)]
		i += 5
	b += s[(i+1):(i+5)]
	i += 5
	res = int(b,2)
	return (i, res)

def parseOpZ2(s,i):
	length = int(s[i:(i+15)],2)
	i += 15
	end = i + length
	values = []
	while i < end:
		(i, r) = parseOp2(s, i)
		values.append(r)
	return (i, values)

def parseOpO2(s,i):
	num = int(s[i:(i+11)],2)
	i += 11
	values = []
	for _ in range(num):
		(i,r) = parseOp2(s, i)
		values.append(r)
	return (i,values)

def parseOp2(s, i):
	beg = i
	while i < len(s):
		if s[i] == '1':
			break
		i += 1
	if i >= len(s):
		return len(s)
	i = beg
	i += 3
	t = s[i:(i+3)]
	i += 3
	ID = int(t,2)
	if ID == 4:
		(i,v) = parseLit2(s,i)
	else:
		if s[i] == '0':
			(i, values) = parseOpZ2(s,i+1)
		else:
			(i, values) = parseOpO2(s,i+1)
		if ID == 0:
			v = sum(values)
		elif ID == 1:
			v = 1
			for n in values:
				v *= n
		elif ID == 2:
			v = min(values)
		elif ID == 3:
			v = max(values)
		elif ID == 5:
			v = 1 if values[0] > values[1] else 0
		elif ID == 6:
			v = 1 if values[0] < values[1] else 0
		elif ID == 7:
			v = 1 if values[0] == values[1] else 0
	return (i,v)

def part2():
	f = reader()
	h = int(f[0],16)
	start = (format(int(f[0][0],16),"#06b"))
	start = start[2:]
	ind = 0
	b = bin(h)
	s = b[2:]
	while start[ind] == '0':
		s = '0' + s
		ind += 1
	(i,v) = parseOp2(s, 0)
	print(v)
	i = 0

part1()
part2()
