T = int(input())
for i in range(T):
    N, M, K = map(int, input().split())
    total = N * M
    if K == 0:
        print(total)
        continue
    alice_owned = 0
    for i in range(1, M):
        piece = N * i
        if piece >= K:
            alice_owned = max(alice_owned, total - piece)
        piece = N * (M - i)
        if piece >= K:
            alice_owned = max(alice_owned, total - piece)
    for i in range(1, N):
        piece = i * M
        if piece >= K:
            alice_owned = max(alice_owned, total - piece)
        piece = (N - i) * M
        if piece >= K:
            alice_owned = max(alice_owned, total - piece)
    print(alice_owned)