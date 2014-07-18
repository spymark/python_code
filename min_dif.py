
def solution(A):
    B = [0]*len(A)
    for i in range(len(A)):
        if i ==0:
            B[i] = A[i]
        else:
            B[i] = A[i] + B[i-1]
    min = abs(B[-1]-B[0])
    for p in (range(len(B)-1)):
        diff = abs(B[-1]-B[p])
        if abs(diff-B[p]) < min:
            min = abs(diff-B[p])


    return min



A = [3,1,2,4,3]
print solution(A)