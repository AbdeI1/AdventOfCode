import os
os.chdir(os.path.dirname(__file__))

years = range(2015, 2020)
days = range(1, 26)

for y in years:
  yname = f"{y}"
  if not os.path.exists(yname):
    os.mkdir(yname)
  os.chdir(yname)
  for d in days:
    dname = f"{d:02}"
    if not os.path.exists(dname):
      os.mkdir(dname)
    os.chdir(dname)
    os.chdir('..')
  os.chdir('..')
