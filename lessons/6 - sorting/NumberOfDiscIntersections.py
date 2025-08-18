def solution(A):
    l = len(A)

    if l < 2:
        return 0
    
    starts = [0] * l
    ends = [0] * l

    for index in range(l):
        starts[index] = index - A[index]
        ends[index] = index + A[index]
        
    starts.sort()
    ends.sort()

    print(f"starts: {starts}, ends: {ends}")

    result = 0
    count = 0
    j = 0

    for i in range(l):
        while j < l and ends[j] < starts[i]:
            count -= 1
            j += 1
        
        result += count

        if result > 10000000:
            return -1

        count += 1

    return result