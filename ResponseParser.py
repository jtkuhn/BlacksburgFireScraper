import re

outfp = open('OutputFile.json', 'w+', errors='xmlcharrefreplace')
rejectfp = open('RejectFile.json', 'w+', errors='xmlcharrefreplace')

with open('StatusFile.json') as fp:
    pattern = re.compile('\d{2,}')
    for line in fp:
        if pattern.search(line[0:7]):
            outfp.write(line)
        else:
            rejectfp.write(line)
