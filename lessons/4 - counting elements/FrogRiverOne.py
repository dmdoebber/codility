def solution(X, A):
    if len(A) == 1:
        if X == 1:
            return 0
        else:
            return -1

    values = set()
    for index, value in enumerate(A):
        values.add(value)
        if len(values) == X:
            return index
        
    return -1