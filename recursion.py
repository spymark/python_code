# __author__ = 'spyros'
# import test
# def reverse(s):
#     if len(s) == 0:
#         return ''
#     if len(s) == 1:
#         return s
#     if len(s)==2:
#         return s[1]+s[0]
#     if len(s)==3:
#         return s[2] + s[1] +s[0]
#
#     return reverse(s[(len(s)//2):])+ reverse(s[0:len(s)//2])
#
#
#
# def pal(s):
#     s = s.lower()
#     if reverse(s) == s:
#         print True
#     else:
#         print False
#
# pal('Kanakanak')

def countdown(n):
    print(n)

    if n == 0:  # this is the base case
        return  # return, instead of making more recursive calls

    countdown(n - 1)

countdown(10)