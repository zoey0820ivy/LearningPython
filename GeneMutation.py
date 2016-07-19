
def SearchDiff(a, b):
    var = 0
    i = 0
    if len(a) == len(b):
        while (i < len(a)):
            if a[i] != b[i]:
                var += 1
                i += 1
        return var
    else:
        if len(a) > len(b):
            l = len(a) - len(b)
            while (i < len(b)):
                if a[i] != b[i]:
                    var += 1
                    i += 1
            return var + l
        else:
            l = len(b) - len(a)
            while (i < len(a)):
                if a[i] != b[i]:
                    var += 1
                    i += 1
            return var + l

S = SearchDiff("GASSSSSSSS","FFFF")
print(S)