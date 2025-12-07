import os
os.chdir(os.path.dirname(__file__))
import subprocess
from aocd import get_data, submit as aocd_submit

token = ''
with open('.session.txt') as f:
  token = f.read().strip()


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
  return open(f"input.txt", 'r').read().splitlines()


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
  with open(f"{yname(year)}/{dname(day)}/input.txt", 'w', newline='\n') as f:
    f.write(get_data(year=year, day=day, session=token) + '\n')


def submit(year, day):
  out = subprocess.run(
    ['python', f"{yname(year)}/{dname(day)}/code.py"], capture_output=True, text=True).stdout.splitlines()
  if len(out) > 0:
    aocd_submit(out[0], part="a", year=year, day=day, session=token)
  if len(out) > 1:
    aocd_submit(out[1], part="b", year=year, day=day, session=token)


y, d = 2025, 7

fetch(y, d)
submit(y, d)
