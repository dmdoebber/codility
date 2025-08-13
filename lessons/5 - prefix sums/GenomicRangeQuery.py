def solution(S, P, Q):
    l = len(S) + 1

    a_count = [0] * l
    a_sum = 0

    c_count = [0] * l
    c_sum = 0

    g_count = [0] * l
    g_sum = 0

    for index in range(1, l):
        value = S[index - 1]

        if value == 'A':
            a_sum += 1

        elif value == 'C':
            c_sum += 1

        elif value == 'G':
            g_sum += 1

        a_count[index] = a_sum
        c_count[index] = c_sum
        g_count[index] = g_sum

    result = [0] * len(P)

    for index, (p, q) in enumerate(zip(P, Q)):
        start = p
        end = q + 1

        if a_count[end] - a_count[start] > 0:
            result[index] = 1

        elif c_count[end] - c_count[start] > 0:
            result[index] = 2
        
        elif g_count[end] - g_count[start] > 0:
            result[index] = 3

        else:
            result[index] = 4 

    return result