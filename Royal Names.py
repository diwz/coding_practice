def romanNumToInt(s):
    nums = {'I':1, 'V':5, 'X':10, 'L':100}
    total = 0
    s = s[::-1]
    lastChar = None
    for x in s:
        if lastChar and nums[x] < lastChar:
            total -= 2*nums[x]
        total += nums[x]
        last = nums[x]
    return total

def  getSortedList(names):
    data = []
    for n in names:
        data.append(n.split())
    sorted_names = sorted(data, key=lambda d:(d[0], romanNumToInt(d[1])))

    for n in sorted_names:
        print " ".join(n)


data = ["Louis IX", "Louis VIII", "Jack VI", "AJ I", "AJ V"]


