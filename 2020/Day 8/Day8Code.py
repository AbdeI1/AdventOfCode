def part1():
	f = open("C:/Users/bluey/Documents/Coding Projects/AdventOfCode/Day 8/Day8input.txt", 'r').read()
	f = f.split('\n')
	f = f[:len(f) - 1]
	a = [0] * len(f)
	i = 0
	accumaltor = 0
	while(i < len(f)):
		if(a[i] == 1):
			print(accumaltor)
			return False
		else:
			a[i] = 1
			line = f[i]
			if line[:3] == "jmp":
				if line[4] == "+":
					i += int(line[5:])
				else:
					i -= int(line[5:])
			elif line[:3] == "acc":
				if line[4] == "+":
					accumaltor += int(line[5:])
				else:
					accumaltor -= int(line[5:])
				i += 1
			else:
				i += 1
	
def newPart1(f):
	a = [0] * len(f)
	i = 0
	accumaltor = 0
	while(i < len(f)):
		if(a[i] == 1):
			return [False, accumaltor]
		else:
			a[i] = 1
			line = f[i]
			if line[:3] == "jmp":
				if line[4] == "+":
					i += int(line[5:])
				else:
					i -= int(line[5:])
			elif line[:3] == "acc":
				if line[4] == "+":
					accumaltor += int(line[5:])
				else:
					accumaltor -= int(line[5:])
				i += 1
			else:
				i += 1
	return [True, accumaltor]


def part2():
	f = open("C:/Users/bluey/Documents/Coding Projects/AdventOfCode/Day 8/Day8input.txt", 'r').read()
	f = f.split('\n')
	f = f[:len(f) - 1]
	i = 0
	while i < len(f):
		line = f[i]
		if line[:3] == "jmp":
			temp = f[i]
			f[i] = "nop" + line[3:]
			answer = newPart1(f)
			if(answer[0]):
				return answer
			else:
				f[i] = temp
		elif line[:3] == "nop":
			temp = f[i]
			f[i] = "jmp" + line[3:]
			answer = newPart1(f)
			if(answer[0]):
				return answer
			else:
				f[i] = temp
		i += 1




print(part2())