def part1():
    f = open('C:/Users/bluey/Documents/Coding Projects/AdventOfCode/Day 2/Day2input.txt', 'r').read()
    f = f.split('\n')
    result = 0
    for i in range(len(f) - 1):
        a = f[i].split(':')
        policy = a[0]
        password = a[1][1:]
        pChar = policy[len(policy) - 1]
        pMin = int(policy[0:policy.find('-')])
        pMax = int(policy[policy.find('-') + 1: len(policy) - 2])
        count = password.count(pChar)
        if pMin <= count <= pMax:
            result = result + 1
    print(result)


def part2():
    f = open('C:/Users/bluey/Documents/Coding Projects/AdventOfCode/Day 2/Day2input.txt', 'r').read()
    f = f.split('\n')
    result = 0;
    for i in range(len(f) - 1):
        a = f[i].split(':')
        policy = a[0]
        password = a[1][1:]
        pChar = policy[len(policy) - 1]
        pFirst = int(policy[0:policy.find('-')]) - 1
        pSecond = int(policy[policy.find('-') + 1: len(policy) - 2]) - 1
        if bool(password[pFirst] == pChar) != bool(password[pSecond] == pChar):
            result = result + 1
    print(result)


part1()
part2()
