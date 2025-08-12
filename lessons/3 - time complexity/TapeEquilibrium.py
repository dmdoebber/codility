def solution(A):
    l = len(A)

    if l == 1:
        return 0

    forward_values = [0] * (l - 1)
    backward_values = [0] * (l - 1)

    backward_sum = 0
    forward_sum = 0

    for n in range(0, l - 1):
        forward_index = n
        backward_index = l - n - 1

        forward_sum += A[forward_index]
        backward_sum += A[backward_index]

        forward_values[forward_index] = forward_sum
        backward_values[backward_index - 1] = backward_sum

    result = 999999999

    for n in range(0, l - 1):
        diff = forward_values[n] - backward_values[n]
        result = min(result, abs(diff))

    return result