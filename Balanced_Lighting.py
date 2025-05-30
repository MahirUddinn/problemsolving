import math

T = int(input())
for _ in range(T):
    N = int(input())
    C = list(map(int, input().split()))
    red = C.count(1)
    blue = C.count(2)
    unknown = C.count(0)
    if len(C) % 2 != 0:
        print("No")
    else:
        half = math.floor(len(C) / 2)
        ramaining_r = half - red
        remianing_b =  half - blue
        if ramaining_r + remianing_b <= unknown and (unknown - (ramaining_r + remianing_b)) % 2 == 0:
            print("Yes")
        else:
            print("No")