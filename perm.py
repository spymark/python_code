def permute(s):
    res = []
    #if length is 1, we are done
    if len(s) == 1:
        res = [s]
    else:
    #if not, then find the permutations of string length n-1
        for i, c in enumerate(s):
            for perm in permute(s[:i] + s[i+1:]):
                res += [c + perm]

    return res

# print permute('abc')

a = [1,2,3]
a.insert(3,4)
print a