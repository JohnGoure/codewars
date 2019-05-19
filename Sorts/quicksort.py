class Quicksort:

    def sort(self, arr, lo, hi):
        """Sort the collection in O(NlgN) time."""
        if lo < hi:
            pi = self._partition(arr, lo, hi)
            self.sort(arr, lo, pi - 1)
            self.sort(arr, pi + 1, hi)

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
    aux = [4, 2, 1, 0]
    Quicksort().sort(aux, 0, len(aux) - 1)
