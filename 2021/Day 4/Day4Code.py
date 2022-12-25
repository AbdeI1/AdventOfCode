def reader():
	f = open("Day4input.txt", 'r').read()
	f = f.split('\n')
	f = f[:-1]
	return f

def part1():
	f = reader()
	nums = f[0].split(',')
	boards = [[[-2]*5 for i in range(5)] for i in range(100)]
	i = -1
	j = 0
	for l in f[1:]:
		if len(l) == 0:
			i+=1
			j=0
			continue
		line = l.split(' ')
		lk = 0
		for k in range(5):
			if line[lk] == '':
				lk+=1
			boards[i][j][k] = int(line[lk])
			lk+=1
		j+=1
	for n in nums:
		for b in boards:
			for i in range(5):
				for j in range(5):
					if b[i][j] == int(n):
						b[i][j] = -1
						cn1 = 0
						for k in range(5):
							if b[i][k] == -1:
								cn1 += 1
						if cn1 >= 5:
							s = 0
							for k1 in range(5):
								for k2 in range(5):
									if b[k1][k2] != -1:
										s += b[k1][k2]
							print(s * int(n))
							return
						cn1 = 0
						for k in range(5):
							if b[k][j] == -1:
								cn1 += 1
						if cn1 >= 5:
							s = 0
							for k1 in range(5):
								for k2 in range(5):
									if b[k1][k2] != -1:
										s += b[k1][k2]
							print(s*int(n))
							return
	print("bad")

def part2():
	f = reader()
	nums = f[0].split(',')
	boards = [[[-2]*5 for i in range(5)] for i in range(100)]
	i = -1
	j = 0
	for l in f[1:]:
		if len(l) == 0:
			i+=1
			j=0
			continue
		line = l.split(' ')
		lk = 0
		for k in range(5):
			if line[lk] == '':
				lk+=1
			boards[i][j][k] = int(line[lk])
			lk+=1
		j+=1
	bw = 0
	for n in nums:
		for b in boards:
			for i in range(5):
				for j in range(5):
					if b[i][j] == int(n):
						b[i][j] = -1
						cn1 = 0
						for k in range(5):
							if b[i][k] == -1:
								cn1 += 1
						if cn1 >= 5 and bw >= 99:
							s = 0
							for k1 in range(5):
								for k2 in range(5):
									if b[k1][k2] != -1:
										s += b[k1][k2]
							print(s * int(n))
							return
						elif cn1 >= 5:
							for k1 in range(5):
								for k2 in range(5):
									b[k1][k2] = -1
							bw += 1
							continue
						cn1 = 0
						for k in range(5):
							if b[k][j] == -1:
								cn1 += 1
						if cn1 >= 5 and bw >= 99:
							s = 0
							for k1 in range(5):
								for k2 in range(5):
									if b[k1][k2] != -1:
										s += b[k1][k2]
							print(s*int(n))
							return
						elif cn1 >= 5:
							for k1 in range(5):
								for k2 in range(5):
									b[k1][k2] = -1
							bw += 1
	print("bad")

part1()
part2()

