def step(s, m, n):
    aux = []
    for x in range(m, n + 1):
        if checkPrime(x) is True:
            aux.append(x)
    if len(aux) < 2:
        return None
    for x in range(len(aux) - 1):
        if aux[x] + s in aux:
            return [aux[x], aux[aux.index(aux[x] + s)]]
    return None


def checkPrime(x):
    if x == 2 or x == 3: return True
    if x < 2 or x%2 == 0: return False
    if x < 9: return True
    if x%3 == 0: return False
    r = int(x**0.5)
    f = 5
    while f <= r:
        if x%f == 0: return False
        if x%(f+2) == 0: return False
        f +=6
    return True
