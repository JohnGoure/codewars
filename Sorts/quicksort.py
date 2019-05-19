class Quicksort:

    def sort(self, arr, lo, hi):
        """Sort the collection in O(NlgN) time."""
        if lo < hi:
            print(arr)
            pivot = self._partition(arr, lo, hi)
            self.sort(arr, lo, pivot - 1)
            self.sort(arr, pivot + 1, hi)

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

    def demo(arr):
        """Demonstrate quicksort sorting."""

if __name__ == "__main__":
    aux = [12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
    Quicksort().sort(aux, 0, len(aux) - 1)
