def binaryS(n, palindromes):
  l = 0
  r = len(palindromes)-1
  while l <= r:
    if(palindromes[(l+r)//2] < n):
      l = (l+r)//2+1
    else:
      r = (l+r)//2-1
  if palindromes[l] < n:
    return l
  return l-1

T = int(input())
palindromes = set()
for t in range(T):
  N = int(input())
  maxn = 0
  for i in range(100,1000):
    for j in range(i,1000):
      text = str(i*j)
      if(text == text[::-1]):
        palindromes.add(i*j)
  convert = list(palindromes)
  print(convert[binaryS(N, convert)])
