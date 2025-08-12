def solution(A):
    max_value = max(A)

    if max_value != len(A):
        return 0

    if len(A) != len(set(A)):
        return 0
        
    return 1