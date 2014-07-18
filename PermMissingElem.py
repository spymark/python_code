def solution(A):
    N = len(A)
    correct = N*(N+1)/2
    actual = sum(A)

    return N-(actual-correct)+1
    pass

A = [4,2,3]
print solution(A)