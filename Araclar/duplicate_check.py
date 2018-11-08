import sys

lineList = set() 
output = open(sys.argv[2], "w" , encoding="utf8")
for line in open(sys.argv[1], "r", encoding="utf8"):
    if line not in lineList:
        if line[0]== '#':
            pass
        else:
            try:
                output.write((line[:-1]).encode('idna').decode('utf-8') + '\n')
            except:
                print('ERROR: {} '.format(line[:-1]))
        lineList.add(line)
output.close()
