f = open('inputFile.txt','r')
#count=0
for line in f:
    line_split = line.split()
    if line_split[2] == 'P':
        print(line)
#    print(str(count)+line)
#    count=+1

#print(f.read())
f.close()
