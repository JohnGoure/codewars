class BubbleSort:
    def sort(self, arr):
        for x in range(len(arr) - 1, 0, -1):
            for y in range(x):
                if arr[y] > arr[y+1]:
                    arr[y], arr[y + 1] = arr[y + 1], arr[y]
        return arr
