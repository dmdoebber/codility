def solution(N):
    values = bin(N)[2:]
    
    result = 0
    
    gap = 0
    started = False
    
    for value in values:
        if value == '1':
            if started: 
                result = max(result, gap)
                gap = 0
            else:
                started = True

        elif started:  
            gap += 1
    
    return result