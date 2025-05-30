T = int(input())
for _ in range(T):
    X, Y, K = map(int, input().split())
    a1 = max((X + 1) // 2, Y)
    a2 = max((Y + 1) // 2, X)
    if min(a1, a2) <= K:
        print("Alice")
    else:
        print("Bob")
        
