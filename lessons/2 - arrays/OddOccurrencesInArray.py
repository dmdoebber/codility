def solution(A):
    result = 0

    for value in A:
        result ^= value 

    return result