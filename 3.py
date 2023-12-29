def findBiggest(arr, biggest):
    if (len(arr) == 0): return biggest
    current = arr[len(arr)-1]
    arr.pop()
    if (current > biggest): return findBiggest(arr, current)
    else: return findBiggest(arr, biggest)
    
print(findBiggest([1,2,3,4,5], 0))