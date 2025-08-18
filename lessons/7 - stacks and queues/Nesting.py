def solution(S):
    l = len(S)
    count = 0

    for index in range(l):
        if S[index] == '(':
            count += 1

        elif S[index] == ')':
            count -= 1

            if count < 0:
                return 0
            
    if count == 0:
        return 1
    else:
        return 0