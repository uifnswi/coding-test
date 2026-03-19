def solution(arr):
    start = 0
    end = 0
    answer = []
    
    if 2 not in arr:
        return [-1]
    
    for i in range(len(arr)):
        if arr[i] == 2:
            start = i
            break
    
    for i in range(len(arr)-1, -1, -1):
        if arr[i] == 2:
            end = i
            break
    
    for i in range(start, end+1):
        answer.append(arr[i])
    
    return answer