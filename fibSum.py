def fibGen(n):
    fibs = []
    a, b = 1, 1
    while b <= n:
        a, b = b, a+b
        fibs.insert(0, a)
    return fibs

def fibSum(n):
    res = []
    fibs = fibGen(n)
    while n > 0:
        if n in fibs:
            res.append(n)
            break
        else:
            n = n - fibs[0]
            res.append(fibs[0])
            for i in range(1, len(fibs)):
                if fibs[i] <= n:
                    fibs = fibs[i:]
                    break
    print(res)
