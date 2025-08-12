def solution(A):
    values = set()

    for value in A:
        if value > 0:
            values.add(value)

    for value in range(1, len(values) + 2):
        if not value in values:
            return value
    
    return 1