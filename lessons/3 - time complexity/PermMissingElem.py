def solution(A):
    l = len(A)
    result = 0
    
    for index in range(1, l + 2):
        result ^= index
  
    for value in A:
        result ^= value

    return result