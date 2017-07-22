import re

outfp = open('output/OutputFile.txt', 'w+', errors='xmlcharrefreplace')
rejectfp = open('output/RejectFile.txt', 'w+', errors='xmlcharrefreplace')

with open('output/StatusFile.txt') as fp:
    pattern = re.compile('\d{2,}')
    for line in fp:
        if pattern.search(line[0:7]):
            outfp.write(line)
        else:
            rejectfp.write(line)
