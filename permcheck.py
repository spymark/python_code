def solution(A):
    N = len(A)
    ans = 0
    B={}
    for i in range(len(A)):
        if A[i] in B.keys():
            return 0
        elif i==0:
            B[A[i]] = A[i]
        else:
            B[A[i]] = A[i]+B[A[i-1]]
    if B[A[-1]] == N*(N+1)/2:
        return 1

    return ans


A = [1,2,4]
print solution(A)