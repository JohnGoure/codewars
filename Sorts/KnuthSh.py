import random
import math
def ShellSort(arr):
    n = len(arr)
    gap = 1
    while gap < math.ceil(n/3):
        gap*3 + 1
    
    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i
            while j > gap - 1 and arr[j - gap] >= temp:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp
        gap = math.ceil((gap - 1)/3)

mock = random.sample(range(100), 30)
print(ShellSort(mock))