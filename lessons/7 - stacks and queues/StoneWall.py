def solution(H):
    stack = []
    result = 0

    for value in H:
        while stack and stack[-1] > value:
            stack.pop()

        if not stack or stack[-1] < value:
            stack.append(value)
            result += 1

    return result