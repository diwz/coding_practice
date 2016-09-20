import re


def plagiarismCheck(code1, code2):
    var = re.compile(r"([_a-zA-Z]\w*)")
    if len(code1) != len(code2):
        return False
    map = {}
    var_set = set()
    for l1, l2 in zip(code1, code2):
        m1 = var.findall(l1)
        n1 = var.sub("", l1)
        m2 = var.findall(l2)
        n2 = var.sub("", l2)
        if n1 != n2 or len(m1) != len(m2):
            return False
        for v1, v2 in zip(m1, m2):
            if v1 != v2:
                if v1 in map and map[v1] != v2:
                    return False
                else:
                    if v1 in var_set:
                        return False
                    else:
                        map[v1] = v2
            else:
                if v1 in map:
                    return False
                var_set.add(v1)
    return True
