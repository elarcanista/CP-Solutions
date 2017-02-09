import re, sys

prog = re.compile(r'[a-zA-Z]+')

for inp in sys.stdin: 
  print(len(re.findall(prog,inp)))
