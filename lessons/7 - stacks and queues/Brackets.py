def solution(S):
    stack = []
    pairs = {')': '(', ']': '[', '}': '{'}

    open_values = pairs.values()

    for value in S:
        if value in open_values:
            stack.append(value)
        else:
            if not stack: 
                return 0
            
            if stack[-1] != pairs[value]: 
                return 0
            
            stack.pop()

    if stack:
        return 0
    else:
        return 1