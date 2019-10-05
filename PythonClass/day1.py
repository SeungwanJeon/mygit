print('hello')

7/3
7//3
7%3
2**3
2**4+5
3*5**2


a=10.
type(a)
b=int(a)
type(b)
c=str(b)
print(c)
type(c)


aaa=input("enter variable aaa")
print(aaa)
type(aaa)

print("%.3d"%(2))


F=float(input("enter input"))
C=(F-32)*5/9
print("화씨: %.2f\n 섭씨: %f" %(F,C))

"""
장문의
주석처리이다
"""

'python'+'is'
'py'*2


a='python'
a[0:4:2]
a[::-1]

'o'in a
'x' in a
'on' in a
len(a)
b='pnytthon'
b.count('n')
b.count('tt')
b.index('n')
b.join(',,')

'\\'.join(['a','bb'])

print(a)
print(a[-1])
print(a[len(a)-1])

b='abc:d2f:g2e'
print(b.split(':'))
c=' '.join(b.split(':'))
print(c)
print(c.split())
c.split('2')

fruit=['banana',3.,'cherry']
print(fruit)
type(fruit)
fruit[0]
fruit*2
fruit[1:2]=[]
fruit=['banana',3.,'cherry']
del fruit[0]
fruit
fruit=['banana',3.,'cherry']
del fruit[0:1]
fruit


t=[1,2,3]
a,b,c=t
print(a,b,c)

date=input('날짜입력 yyyy/mm/dd')
y,m,d=(map(int,date.split('/')))
print('10년 뒤는 %d년 %d월 %d일'%(y+10,m,d))

5<6<7



def ispass(eng,math):
    if eng+math<=110:
        print("총합 점수 부족")
    elif eng<=40:
        print("영어 점수 부족")
    elif math<=40:
        print("수학 점수 부족")
    else:
        print("합격")
ispass(80,20)
ispass(90,30)
ispass(70,80)
ispass(35,30)
ispass(35,95)

count=0
while count<5:
    print(end="hello ")
    count+=1

count=1
val_sum=0
while count<=10:
    val_sum+=count
    count+=1
print(val_sum)

count=1
val_mult=1
while count<=10:
    val_mult*=count
    count+=1
print(val_mult)


x0=3159
x1=' '.join(str(x0)).split()
for idx0 in range(len(x1)):
    for idx1 in range(int(x1[idx0])):
        print('*',end='')
    print('')

for x in str(x0):
    print('*'*int(x))


f=['banana','apple','orange']
f.sort()
print(f)
f.sort(reverse=1)
print(f)
f.reverse()
print(f)
f=['banana','apple','orange']
sorted(f)

flag=1
array=list()
while flag:
    x=input('enter a number')
    if x!='Done':
        array.append(int(x))
    else:
        flag=0

print('average: %.2f, max: %.2f, min: %.2f' \
    %(sum(array)/len(array),max(array),min(array)))


[idx0*idx1 for idx0 in range(2,10) for idx1 in range(1,10)]

[x for x in range(1,6) if x%2==0]

L1=[1,2,3]
L2=[3,4,5]
[x*y for x in L1 for y in L2]
