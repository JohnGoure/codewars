import random


class Quicksort:

    def sort(self, arr):
        """Sort the collection in O(NlgN) time."""
        random.shuffle(arr)
        self._sort(arr, 0, len(arr) - 1)

    def _sort(self, arr, lo, hi):
        if lo < hi:
            pi = self._partition(arr, lo, hi)
            self._sort(arr, lo, pi - 1)
            self._sort(arr, pi + 1, hi)

    def _partition(self, arr, lo, hi):
        """Place the pivot element at its correct position in the sorted array."""
        i = lo - 1
        pivot = arr[hi]

        for j in range(lo, hi):
            if arr[j] <= pivot:
                i = i+1
                arr[i], arr[j] = arr[j], arr[i]
        arr[i+1], arr[hi] = arr[hi], arr[i+1]
        return i+1

if __name__ == "__main__":
    aux = [4, 2, 1, 0, 10, 12, 14, 11, 22, 65, 43, 25, 86, 91]
    Quicksort().sort(aux)
    print(aux)
