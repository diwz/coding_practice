n = int(raw_input())

data = []
for i in range(n):
    data.append(map(int, raw_input().split()))

data.sort(reverse=True, key=lambda d: d[0])

res = []
print data
if n >= 1:
    cmax = data[0][1]
res.append(data[0])
for i in range(1, n):
    if cmax < data[i][1]:
        res.append(data[i])
        cmax = data[i][1]
print res
