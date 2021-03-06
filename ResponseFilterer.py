import re


#This acts as the initial filter that separates tweets appearing to have dates from those without
#Ideally, all tweets ending in the output file are parsable and all tweets send to the reject pile aren't.
def filterResponses():
    containsManyDigitsPattern = '\d{3,}'

    inputFile = 'output/StatusFile.txt'
    outfp = open('output/OutputFile.txt', 'w+', errors='xmlcharrefreplace')
    rejectfp = open('output/RejectFile.txt', 'w+', errors='xmlcharrefreplace')

    with open(inputFile) as fp:
        pattern = re.compile(containsManyDigitsPattern)
        for line in fp:
            if pattern.search(line[0:7]):
                outfp.write(line)
            else:
                rejectfp.write(line)


if __name__ == "__main__":
    filterResponses()