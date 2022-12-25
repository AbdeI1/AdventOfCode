def reader():
	f = open("Day1input.txt", 'r').read()
	f = f.split('\n')
	f = f[:-1]
	return f

def part1():
	f = reader()
	count = 0
	for i in range(len(f) - 1):
		if(int(f[i+1]) > int(f[i])):
			count+=1
	print(count)

def part2():
	f = reader()
	count = 0
	for i in range(len(f) - 3):
		if(int(f[i+1]) + int(f[i+2]) + int(f[i+3]) > int(f[i]) + int(f[i+1]) + int(f[i+2])):
			count+=1
	print(count)

part1()
part2()
