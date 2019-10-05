import sys

args=sys.argv[1:]

try:
    f1=open(args[0],'r')
except:
    print('%s cannot be found'%args[0])
else:
    f2=open(args[1],'w')
    f2.write(f1.read())
    f1.close()
    f2.close()
