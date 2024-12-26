def reader():
	f = open("C:/Users/bluey/Documents/Coding Projects/AdventOfCode/Day 19/Day19input.txt", 'r').read().split("\n\n")
	return f


def part1():
	f = reader()
	rules = f[0].split('\n')
	messages = f[1].split('\n')
	rules = sort(rules)
	i = 0
	while i < len(rules):
		rules[i] = rules[i][rules[i].index(':') + 2:]
		i += 1
	total = 0
	for m in messages:
		f = followsRule(m, 0, rules)
		if f[0] and f[1] == len(m):
			total += 1
	print(total)


def part2():
	f = reader()
	rules = f[0].split('\n')
	messages = f[1].split('\n')
	rules = sort(rules)
	i = 0
	while i < len(rules):
		rules[i] = rules[i][rules[i].index(':') + 2:]
		i += 1
	rules[8] = "42 | 42 42 | 42 42 42 | 42 42 42 42 | 42 42 42 42 42 | 42 42 42 42 42 42 | 42 42 42 42 42 42 42 | 42 42 42 42 42 42 42 42 | 42 42 42 42 42 42 42 42 42 | 42 42 42 42 42 42 42 42 42 42 | 42 42 42 42 42 42 42 42 42 42 42"
	rules[11] = "42 31 | 42 42 31 31 | 42 42 42 31 31 31 | 42 42 42 42 31 31 31 31 | 42 42 42 42 42 31 31 31 31 31 | 42 42 42 42 42 42 31 31 31 31 31 31 | 42 42 42 42 42 42 42 31 31 31 31 31 31 31 | 42 42 42 42 42 42 42 42 31 31 31 31 31 31 31 31 | 42 42 42 42 42 42 42 42 42 31 31 31 31 31 31 31 31 31 | 42 42 42 42 42 42 42 42 42 42 31 31 31 31 31 31 31 31 31 31"
	total = 0
	for m in messages:
		s = m
		segments1 = []
		i = 0
		p = followsRule(s, 8, rules)
		while p[0]:
			i += p[1]
			segments1.append(i)
			p = followsRule(s[i:], 8, rules)
		segments2 = []
		for segment in segments1:
			segments2.append(followsRule(s[segment:], 11, rules)[1])
		i = 0
		print(segments1)
		print(segments2)
		print(len(s))
		while i < len(segments1):
			if not (segments1[i] == 0 or segments2[i] == 0):
				if segments1[i] + segments2[i] == len(s):
					print("True")
					total += 1
					break
			i += 1
	print(total)



def followsRule(s, i, rules):
	if len(s) == 0:
		return [False, 0]
	if "\"" in rules[i]:
		return [s[0] == rules[i][1], 1]
	else:
		r = rules[i].split('|')
		for rule in r:
			#print("rule " + str(i) + ": " + rule)
			nums = list(filter(lambda x: x != '', rule.split(' ')))
			result = [True, 0]
			length = 0
			for num in nums:
				n = int(num)
				# print(n)
				p = followsRule(s[length:], n, rules)
				if p[0]:
					length += p[1]
				else:
					result[0] = False
					break
			if result[0]:
				return [True, length]
		#print(r)
		#print(s)
		return [False, -1]



def sort(rules):
	i = 0
	while i < len(rules):
		j = 0
		while j < len(rules):
			if int(rules[j][0:rules[j].index(':')]) == i:
				temp = rules[i]
				rules[i] = rules[j]
				rules[j] = temp
			j += 1
		i += 1
	return rules


part2()
