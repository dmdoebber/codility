import math

def solution(A, B, K):
    div_b = math.floor(B / K)
    div_a = math.floor((A - 1) / K)

    return div_b - div_a