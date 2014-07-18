def solution(A):
    # write your code in Python 2.7
    total_sum= 0
    for i in A:
        total_sum = total_sum + i



    running_sum =0
    idx = 0
    for j in A:
        cond = (total_sum - j) / 2.0

        if running_sum == cond:
            return idx
        running_sum += j
        idx+=1

    return -1

# # A = [-7, 1, 5, 2, -4, 3, 0]
# sol = solution(A)
# print '----'
# print sol