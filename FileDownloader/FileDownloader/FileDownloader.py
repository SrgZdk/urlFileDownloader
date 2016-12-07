import urllib
testfile = urllib.URLopener()
with open('records.txt') as fp:
    for line in fp:
        print line
        #filename = line[-49:-1]
        filename = line.split('/')[-1].rstrip()
        testfile.retrieve(line, filename)