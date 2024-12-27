import os
os.chdir(os.path.dirname(__file__))
from aocd import get_data, submit

years = range(2015, 2020)
days = range(1, 26)


def yname(y): return f"{y}"
def dname(d): return f"{d:02}"


def init(years, days):
  for y in years:
    if not os.path.exists(yname(y)):
      os.mkdir(yname(y))
    os.chdir(yname(y))
    for d in days:
      if not os.path.exists(dname(d)):
        os.mkdir(dname(d))
      os.chdir(dname(d))
      if not os.path.exists('code.py'):
        with open('code.py', 'w') as f:
          f.write("""import os
os.chdir(os.path.dirname(__file__))


def reader():
  return open(f"input.txt", 'r').read().split('\\n')[:-1]


def part1():
  pass


def part2():
  pass


part1()
part2()
""")
      os.chdir('..')
    os.chdir('..')


def fetch(year, day):
  os.chdir(f"{yname(year)}/{dname(day)}")
  with open('input.txt', 'w') as f:
    f.write(get_data(year=year, day=day) + '\n')


init(years, days)
