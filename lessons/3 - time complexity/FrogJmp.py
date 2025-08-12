import math

def solution(X, Y, D):

    dist = Y - X
    result = math.ceil(dist / D)

    return result