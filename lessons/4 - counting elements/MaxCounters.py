def solution(N, A):
    max_inc_value = N + 1

    max_count = 0
    max_last = 0

    values = N * [0]

    for value in A:
        if value == max_inc_value:
            max_last = max_count
        else:
            index = value - 1 

            if values[index] < max_last: 
                values[index] = max_last 

            values[index] += 1
            max_count = max(max_count, values[index])

    for index in range(0, N):
        if values[index] < max_last:
            values[index] = max_last    
    
    return values