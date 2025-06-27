t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    answer = a[0]

    for i in range(1, n):
        time = max(a[i] + 1, i)
        answer = min(answer, time)

    print(answer)
