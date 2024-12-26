def reader():
	f = open("C:/Users/bluey/Documents/Coding Projects/AdventOfCode/Day 18/Day18input.txt", 'r').read()
	f = f.split('\n')
	f = f[: len(f) - 1]
	return f


def part1():
	f = reader() #reads .txt and returns string list
	total = 0
	for s in f:
		total += int(solve(s))
	print(total)


def part2():
	f = reader() #reads .txt and returns string list
	total = 0
	for s in f:
		total += int(solve(putParen(s)))
	print(total)


def evaluate(s):
	equation = s.split(' ')
	total = int(equation[0])
	i = 0
	while i < len(equation) - 2:
		if equation[i + 1] == '+':
			total += int(equation[i + 2])
		elif equation[i + 1] == '*':
			total *= int(equation[i + 2])
		i += 2
	return total


def getParen(s):
	if '(' in s:
		i = s.index('(') + 1
		order = 1
		while i < len(s):
			if s[i] == '(':
				order += 1
			if s[i] == ')':
				order -= 1
			if order == 0:
				return [s[s.index('(') + 1 : i], s.index('('), i]
			i += 1
	else:
		return [s, -1, -1]


def solve(s):
	if '(' not in s:
		return str(evaluate(s))
	else:
		l = getParen(s)
		return str(solve(s[0 : l[1]] + solve(l[0]) + s[l[2] + 1: ]))


def putParen(s):
	i = 0
	equation = s.split(' ')
	while i < len(equation) - 2:
		if equation[i + 1] == '+':
			if ')' not in equation[i]:
				equation[i] = '(' + equation[i]
			elif ')' in equation[i]:
				j = i
				order = 0
				while j > -1:
					if ')' in equation[j]:
						order += equation[j].count(')')
					if '(' in equation[j]:
						order -= equation[j].count('(')
					if order <= 0:
						equation[j] = '(' + equation[j]
						j = 0
					j -= 1
			if '(' not in equation[i + 2]:
				equation[i + 2] = equation[i + 2] + ')'
			elif '(' in equation[i + 2]:
				j = i + 2
				order = 0
				while j < len(equation):
					if '(' in equation[j]:
						order += equation[j].count('(')
					if ')' in equation[j]:
						order -= equation[j].count(')')
					if order <= 0:
						equation[j] = equation[j] + ')'
						j = len(equation)
					j += 1
		i += 1
	snew = ""
	for x in equation:
		snew += " " + x
	return snew[1:]


def sameParen(s):
	return s.count('(') == s.count(')')


part1()
part2()