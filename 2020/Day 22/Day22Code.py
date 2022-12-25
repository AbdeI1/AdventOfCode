def reader():
	f = open("C:/Users/bluey/Documents/Coding Projects/AdventOfCode/Day 22/Day22input.txt", 'r').read().split("\n")
	return f[:-1]


def part1():
	f = reader()
	player1 = list(map(lambda x: int(x), f[1:26]))
	player2 = list(map(lambda x: int(x), f[-25:]))
	while 0 < len(player1) < 50:
		if player1[0] > player2[0]:
			player1.append(player1[0])
			player1.append(player2[0])
			del player1[0]
			del player2[0]
		elif player1[0] < player2[0]:
			player2.append(player2[0])
			player2.append(player1[0])
			del player1[0]
			del player2[0]
	t = player1 if len(player1) > len(player2) else player2
	i = 0
	score = 0
	print(t)
	while i < len(t):
		score += (t[i] * (len(t) - i))
		i += 1
	print(score)


def part2():
	f = reader()
	player1 = list(map(lambda x: int(x), f[1:26]))
	player2 = list(map(lambda x: int(x), f[-25:]))
	t = play(player1, player2)
	i = 0
	score = 0
	print(t)
	while i < len(t[1]):
		score += (t[1][i] * (len(t[1]) - i))
		i += 1
	print(score)


def play(player1, player2):
	totalCards = len(player1) + len(player2)
	rounds = []
	while 0 < len(player1) < totalCards:
		if [player1, player2] in rounds:
			return [0, player1]
		else:
			rounds.append([list(player1), list(player2)])
			if len(player1) > player1[0] and len(player2) > player2[0]:
				if play(player1[1 : player1[0] + 1], player2[1 : player2[0] + 1])[0] == 0:
					player1.append(player1[0])
					player1.append(player2[0])
					del player1[0]
					del player2[0]
				else:
					player2.append(player2[0])
					player2.append(player1[0])
					del player1[0]
					del player2[0]
			else:
				if player1[0] > player2[0]:
					player1.append(player1[0])
					player1.append(player2[0])
					del player1[0]
					del player2[0]
				elif player1[0] < player2[0]:
					player2.append(player2[0])
					player2.append(player1[0])
					del player1[0]
					del player2[0]
	if len(player1) == totalCards:
		return [0, player1]
	else:
		return [1, player2]




part2()