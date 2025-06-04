def solve():
    N = int(input())
    A = list(map(int, input().split()))

    marker_value = N + 1 
    min_found_length = marker_value

    for i in range(N):
        for j in range(i, N):
            subArray_len = j - i + 1
            if subArray_len < 2:
                continue
            val1 = -1 
            val2 = -1
            distinct_values = 0
            good_Value = True 

            for k in range(i, j + 1): 
                element = A[k]
                
                if distinct_values == 0:
                    val1 = element
                    distinct_values = 1
                elif distinct_values == 1:
                    if element != val1:
                        val2 = element
                        distinct_values = 2
                elif distinct_values == 2: 
                    if element != val1 and element != val2:
                        good_Value = False
                        break 
            if good_Value and distinct_values == 2:
                
                if subArray_len < min_found_length:
                    min_found_length = subArray_len
            
    if min_found_length == marker_value: 
        print("-1")
    else:
        print(min_found_length)

T = int(input())
for _ in range(T):
    solve()
