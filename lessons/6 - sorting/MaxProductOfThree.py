def solution(A):
    A.sort(reverse=True)

    ppp = A[0] * A[1] * A[2]
    pnn = A[0] * A[-1] * A[-2]

    return max(ppp, pnn)