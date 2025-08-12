def solution(A):
    result = 0
    mult = 0

    for value in A:
        if value == 0:
            mult += 1
        else:
            result += mult    

            if result > 1000000000:
                return -1

    return result