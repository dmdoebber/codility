def solution(A):
    l = len(A)
    if l < 3:
        return 0

    A.sort()

    for i in range(l - 2):
        p = A[i]
        q = A[i + 1]
        r = A[i + 2]

        if p + q > r:
            return 1
        
    return 0