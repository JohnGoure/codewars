def min_value(digits):
    return int(''.join(str(e) for e in sorted(list(set(digits)))))

print(min_value([4, 8, 1, 4]))
