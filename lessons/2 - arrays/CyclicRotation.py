def solution(A, K):
    l = len(A)

    if l == 0:
        return A

    rotation = l - (K % l)

    return A[rotation:] + A[0:rotation]