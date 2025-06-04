import math

A, B = map(int, input().split())

total_slices = (A+1) * 4 + (B * 3)

needed = math.ceil(total_slices / 8)

print(needed)
