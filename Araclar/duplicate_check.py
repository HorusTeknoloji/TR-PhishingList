import sys
import whois

lineList = set() 
output = open(sys.argv[2], "w" , encoding="utf8")
for line in open(sys.argv[1], "r", encoding="utf8"):
    if line not in lineList:
        if line[0]== '#':
            pass
        else:
            output.write((line[:-1]).encode('idna').decode('utf-8') + '\n')
        lineList.add(line)
output.close()
