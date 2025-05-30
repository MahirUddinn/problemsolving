T = int(input())

for _ in range(T):
    N = int(input())
    A = list(map(int, input().split()))
    odd_sum = 0
    even_sum = 0
    for i in range(N):
        if i % 2 == 0:
            odd_sum += A[i]
        else:
            even_sum += A[i]
    
    if odd_sum > even_sum:
        print(odd_sum)
    else:
        print(even_sum)
