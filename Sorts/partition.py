def partition(arr, low, high):
    mid = arr[len(arr) // 2]    
    if arr[low] > arr[high]:
        low, high = high, low
    if arr[mid] > arr[high]:
        mid, high = high, mid
    if arr[low] > arr[mid]:
        low, mid = mid, low

    left = low
    right = high 
