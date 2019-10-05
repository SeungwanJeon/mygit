

f=open('students.txt','r')
f.readlines()
f.close()


f=open('new.txt','w')
for i in range(1,6):
    data='%d line\n' % i
    f.write(data)
f.close()

f=open('new.txt','r')
line=f.readline()
f.close()
print(line, end='')

f=open('new.txt','r')
line=f.readlines()
f.close()
print(line)

set(word.replace('\n','') for word in line)

# line[0].strip()

import os
os.path.exists('text.txt')
os.path.exists('new.txt')


f=open('new.txt','a')
for i in range(6,8):
    data='%d line\n' % i
    f.write(data)
f.close()

f=open('new.txt','r')
line=f.readlines()
f.close()
print(line)

# 자동으로 close됨
with open('new1.txt','w') as f:
    f.write('python is fun!')

with open('new1.txt','r') as f:
    print(f.tell())
with open('new1.txt','r') as f:
    f.readline()
    print(f.tell())
with open('new1.txt','r') as f:
    f.seek(5)
    print(f.readline())



a=[[7,2,3],[4,3,2]]
a.sort(key=lambda x:x[2])
a
