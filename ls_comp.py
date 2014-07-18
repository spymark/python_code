# __author__ = 'spyrosmarketos'
# import time
# def maxl(lista):
#
#     maxim = lista[0]
#     minim = lista[0]
#     for i in lista:
#         if i > maxim:
#             maxim = i
#         else:
#             minim = i
#
#
#     return minim,maxim
#
#
# print "Max, Min: " ,maxl([1,2,3,4,5,7])

# def anagram(s1,s2):
#     for i in s1:
#         if i in s2:
#             continue
#         else:
#             return 'No'
#     return 'yes'
#
# print anagram('paok', 'paka')
#
# print 5//2


# s = []
# for i in range(10):
#     s.append(i)
# print s
# s.pop()
# print s.pop(),'\n',s

def revstring(input):
    stack = []
    result=''
    for i in input:
        stack.append(i)
    while stack!=[]:
        result = result+stack.pop()
    return result

print revstring('tokaluteropaidi')

