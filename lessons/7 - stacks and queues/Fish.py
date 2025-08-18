def solution(A, B):
    l = len(A)
    
    stack = []
    result = 0

    for index in range(l):
        fish_size = A[index]
        fish_direction = B[index]
        
        if fish_direction == 1:
            stack.append(fish_size)
        else:
            while stack and fish_size > stack[-1]:
                stack.pop()

            if not stack:
                result += 1
            
    return result + len(stack)