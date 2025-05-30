T = int(input())

for _ in range(T):
    N = int(input())
    A = list(map(int, input().split()))
    
    found = False
    for num in A:
        if num % 3 == 0:
            found = True
            break
    if not found:
        for i in range(N):
            for j in range(i + 1, N):
                if (A[i] + A[j]) % 3 == 0:
                    found = True
                    break
            if found:
                break
    
    if not found:
        for i in range(N):
            for j in range(i + 1, N):
                for k in range(j + 1, N):
                    if (A[i] + A[j] + A[k]) % 3 == 0:
                        found = True
                        break
                if found:
                    break
            if found:
                break
    
    print("Yes" if found else "No")
