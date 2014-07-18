import re


def read_file(filename):
    f = open(filename,'r')
    output=[]
    for line in f:
        line = re.sub(r'[\n\r]',"",line)
        match = re.match(r'^.*if',line)
        if match:
            output.append(line)
    return output

def print_list(list_name):
    for i in list_name:
        print i




content = read_file('recursion.py')
print_list(content)