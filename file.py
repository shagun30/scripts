import sys

f = open(sys.argv[1],"r")
contents = f.read()
contents=contents.replace('\n',' ')
contents=contents.replace('\r','')
f.close()

f=open('new1.txt',"w")
f.write(contents)
