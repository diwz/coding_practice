def longest_substr_k_unique_chrs(string, k):
    if k == 0:
        return 0
    chr_map = {}
    max_len, start = 0, 0

    for i in range(len(string)):
        c = string[i]
        if c not in chr_map:
            if len(chr_map) == k:
                if max_len < i - start:
                    max_start = start
                max_len = max(max_len, i - start)
                for j in range(start, i):
                    key = string[j]
                    chr_map[key] = chr_map[key] - 1
                    if chr_map[key] == 0:
                        start = j + 1
                        chr_map.pop(key)
                        break
            chr_map[c] = 1
        else:
            chr_map[c] += 1


    max_len = max(max_len, len(string) - start)
    print max_start, max_len
    print string[max_start: max_start + max_len]
    return max_len


if __name__ == '__main__':
    string = "abcbbbbcccbdddadacb"
    k = 2
    longest_substr_k_unique_chrs(string, k)
