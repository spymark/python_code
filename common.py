__author__ = 'spyros'


def common(source,target):
    result = []
    for i,c in enumerate(source):
        if c in result:
            continue
        elif c in target:
            result.append(c)
    return result



print common([1,1,2,3],[1,1,2,4])
print common('','')