# Merge sort
# Time : O(N Log N)
# Space: O(N)

def mergeSort(arr):
    n = len(arr)
    if n < 2:
        return
    mid = n // 2
    left = arr[:mid]
    right = arr[mid:]
    mergeSort(left) # divide
    mergeSort(right)
    merge(left,right,arr) # merge

def merge(left,right,arr):
    leftLen = len(left)
    rightLen = len(right)
    i = j = k = 0
    while i < leftLen and j < rightLen:
        if left[i] <= right[j]:
            arr[k] = left[i]
            k += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1
    
    while i < leftLen:
        arr[k] = left[i]
        i += 1
        k += 1
    
    while j < rightLen:
        arr[k] = right[j]
        j += 1
        k += 1

arr = [9,8,7,6,5,4,3,2,1]

mergeSort(arr)
print(arr)