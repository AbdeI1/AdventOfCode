def reader():
	f = open("Day24input.txt", 'r').read()
	f = f.split('\n')
	f = f[:-1]
	return f

def execute(ins, inp):
	reg = {'w': 0, 'x':0, 'y':0, 'z':0}
	j = 0
	for l in ins:
		i = l.split(' ')
		if i[0] == 'inp':
			reg[i[1]] = inp[j]
			j += 1
		elif i[0] == 'add':
			reg[i[1]] = reg[i[1]] + (reg[i[2]] if i[2] in reg else int(i[2]))
		elif i[0] == 'mul':
			reg[i[1]] = reg[i[1]] * (reg[i[2]] if i[2] in reg else int(i[2]))
		elif i[0] == 'div':
			reg[i[1]] = reg[i[1]] // (reg[i[2]] if i[2] in reg else int(i[2]))
		elif i[0] == 'mod':
			reg[i[1]] = reg[i[1]] % (reg[i[2]] if i[2] in reg else int(i[2]))
		elif i[0] == 'eql':
			reg[i[1]] = 1 if reg[i[1]] == (reg[i[2]] if i[2] in reg else int(i[2])) else 0
		else:
			print("failure: ", l)
			return reg
	return reg

def toList(i): return list(map(int, list(str(i))))

def findEquations(f):
	res = []
	st = []
	dig = 0
	for i in range(len(f)):
		if f[i] == "div z 1":    # push onto stack
			st.append((dig, int(f[i+11].split(' ')[2])))
			dig += 1
		elif f[i] == "div z 26": # pop off of stack
			(d, s) = st.pop()
			s += int(f[i+1].split(' ')[2])
			if s < 0:
				res.append("d" + str(d) + " - " + str(abs(s)) + " = " + "d" + str(dig))
			elif s > 0:
				res.append("d" + str(d) + " + " + str(s) + " = " + "d" + str(dig))
			else:
				res.append("d" + str(d) + " = " + "d" + str(dig))
			dig += 1
	return res

def solveEquationsMax(equations):
	res = [0]*14
	for eq in equations:
		(lhs, rhs) = eq.split(" = ")
		lhs = lhs.split(' ')
		if len(lhs) == 1:
			res[int(lhs[0][1:])] = 9
			res[int(rhs[1:])] = 9
		elif lhs[1] == '+':
			res[int(lhs[0][1:])] = 9 - int(lhs[2])
			res[int(rhs[1:])] = 9
		else:
			res[int(lhs[0][1:])] = 9
			res[int(rhs[1:])] = 9 - int(lhs[2])
	return res

def solveEquationsMin(equations):
	res = [0]*14
	for eq in equations:
		(lhs, rhs) = eq.split(" = ")
		lhs = lhs.split(' ')
		if len(lhs) == 1:
			res[int(lhs[0][1:])] = 1
			res[int(rhs[1:])] = 1
		elif lhs[1] == '+':
			res[int(lhs[0][1:])] = 1
			res[int(rhs[1:])] = 1 + int(lhs[2])
		else:
			res[int(lhs[0][1:])] = 1 + int(lhs[2])
			res[int(rhs[1:])] = 1
	return res

def toInt(l):
	res = 0
	t = 1
	for i in range(1, len(l)+1):
		res += l[-i] * t
		t *= 10
	return res

def part1():
	f = reader()
	print(toInt(solveEquationsMax(findEquations(f))))

def part2():
	f = reader()
	print(toInt(solveEquationsMin(findEquations(f))))

part1()
part2() 

