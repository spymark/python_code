from __future__ import division

def solution(X,Y,D):

    if (Y-X)%D >0:
        return ((Y-X)//D) +1
    return (Y-X)//D

print solution(10,85,30)


# def solution(X, Y, D):
#     # write your code in Python 2.7
#     n = 0
#     while(n<(Y-X)/D):
#         print (Y-X)/D
#         n+=1
#     return n
#     pass
#
