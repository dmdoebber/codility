def get_prefix_sum(A):
    l = len(A) + 1
    
    result = [0] * l

    for index in range(1, l):
        result[index] = result[index - 1] + A[index - 1]

    return result

def get_sum(A, start, end):
    return A[end + 1] - A[start]

def get_average(A, start, end):
    count = end - start + 1
    return get_sum(A, start, end) / count