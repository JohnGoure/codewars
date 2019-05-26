def compute_depth(n):
    digits = set()
    i = 0

    while len(digits) != 10:
        i += 1
        digits.update(str(n * i))

    return i

if __name__ == '__main__':
    print(compute_depth(42))
