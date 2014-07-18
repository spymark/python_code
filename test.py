import string
A = [6, 10, 6, 9, 7, 8]


def solution(A):
    map = {}

    for e in A:
        if e in map.keys():
            map[e] += 1
        else:
            map[e] = 1

    # print map

    sorted_keys = sorted(map)

    result = 0
    for i in range(len(sorted_keys) - 1):

        e1 = sorted_keys[i]
        e2 = sorted_keys[i+1]

        sum = map[e1] + map[e2]
        if e2 - e1 == 1 and sum > result:
            result = sum

    return result

print solution(A)
