def solution(A):
    l = len(A)
    
    min_avg = 10000
    result = 0

    for index in range(l - 1):
        avg = sum(A[index:index+2]) / 2
        if avg < min_avg:
            result = index
            min_avg = avg

        if index + 2 < l:
            avg = sum(A[index:index+3]) / 3          

            if avg < min_avg:
                result = index
                min_avg = avg

    return result
