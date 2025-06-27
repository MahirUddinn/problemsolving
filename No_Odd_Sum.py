t = int(input())
for i in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    num_of_ones = a.count(1)
    twos = a.count(2)

    if num_of_ones % 2 != 0:
        print(twos)
    else:
        print(min(num_of_ones // 2, twos))