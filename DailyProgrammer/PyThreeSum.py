class PythagoreanThreeSum:   
    def findAll(self, num):
        self.arr = []
        for x in range(1, num):
            for y in range(x + 1, num):
                for z in range(y + 1, num):
                    if x ** 2 + y ** 2 == z ** 2 and x + y + z == num:
                        self.arr.append([x, y, z])
        return self.arr

    def findAllFaster(self, num):
        self.arr = []

        a = 1
        while a < num - 2:
            b = a + 1
            c = num

            while b < c:
                if a ** 2 + b ** 2 == c ** 2 and a + b + c == num:
                    self.arr.append([a, b, c])
                    b += 1
                    c -= 1
                elif a + b + c > num:
                    c -= 1
                else:
                    b += 1
            a += 1
        return self.arr