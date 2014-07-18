import re

f = open("\\\\aridhia.net\\files\\shared\\Data Science Team\\Genomic Data\\vcf.csv",'r')
output = []
counter = 0
for line in f:
    if counter == 10:
        print 'done'
        break
    line = re.sub(r'[\n\r]','',line)
    # output += line
    print line
    counter+=1

