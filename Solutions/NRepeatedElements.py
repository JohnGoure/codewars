class ElementCounter:
    def repeatedNTimes(self, A):
        self.A = A

        emptySet = set()
        for i in A:
            if i in emptySet:
                return i
            else:
                emptySet.add(i)

counter = ElementCounter()
print(counter.repeatedNTimes([2, 5, 5, 2, 1, 2]))
