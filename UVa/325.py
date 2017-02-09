import re
prog = re.compile(r'[+-]?\d+(\.\d+([eE][+-]?\d+)?|[eE][+-]?\d+)')
str = input().strip()
while str != '*':
  ans = re.fullmatch(prog, str)
  if ans:
    print(str, 'is legal.')
  else:
    print(str, 'is illegal.')
  str = input().strip()
