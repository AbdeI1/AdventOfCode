def part1():
	cardKey = 10943862
	doorKey = 12721030
	subjectNum = 7
	value = 1
	cardLoop = 0
	while True:
		if value == cardKey:
			break
		value = value * subjectNum
		value = value % 20201227
		cardLoop += 1
	value = 1
	subjectNum = doorKey
	for i in range(cardLoop):
		value = value * subjectNum
		value = value % 20201227
	print(value)


part1()
