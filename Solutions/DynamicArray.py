import sys

data = []
for k in range(27):
    a = len(data)
    b = sys.getsizeof(data)
    print('Length: {0:3d}; size in bytes: {1:4d}'.format(a, b))
    data.append(None)
