import math

T = int(input())

for _ in range(T):
  n = int(input())
  base = int(math.sqrt(n))
  result = base * base
  print(result)