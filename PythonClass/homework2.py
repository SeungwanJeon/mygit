"""
문제1-1) 입력 받은 정수가 짝수인지 홀수인지 판별
"""
x=int(input("enter number:"))
def iseven(x):
    if x//2==0:
        print("%d is even" %x)
    else:
        print("%d is odd" %x)
iseven(x)

"""
문제1-2) 프로그래밍 과목의 중간고사와 기말고사 점수를 입력 받아 평균과 학점을 구하는 프로그램을 작성하시오.
"""
score1=70
score2=56
average=(score1+score2)/2
print(average)
def whatgrade (average):
    if average >= 90:
        return 'A'
    elif average >=80:
        return 'B'
    elif average >=70:
        return 'C'
    elif average >=60:
        return 'D'
    else:
        return 'F'
whatgrade(average)

"""
문제1-3) PPT 문제
학생수준평가 시험에서 영어 점수와 수학 점수가 합해서 110점 이상이면 합격이다. 단, 각 점수가 40점 미만
이면 불합격이다. 영어(eng), 수학(math)점수를 입력받아 합격여부를 출력하는 프로그램을 작성하시오.
출력예시는 실습 PPT를 참고하시오
"""
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


"""
문제1-4) PPT 문제
세 개의 정수를 입력 받아, 가장 큰 수만 출력하는 프로그램을 작성하시오. (max 함수 이용하지 않고 구할 것)
세 개의 수를 입력하시오:30 22 50
가장 큰 수는 50입니다.
"""
x=list(map(int,input('enter 3 numbers ex)30 22 50').split()))
maxval=0
for idx in range(len(x)):
    if maxval<=x[idx]:
        maxval=x[idx]
print("가장 큰 수는 %d" %maxval)

"""
문제2-1) 단어(문자열)가 주어질 때, 아래와 같이 출력되도록 작성하시오
P
y
t
h
o
n
"""
word='Python'
for idx in range(len(word)):
    print(word[idx])

"""
문제2-2) 아래와 같이 출력되는 프로그램을 작성하시오.
10,9,8,7,6,5,4,3,2,1,Happynewyear!!
"""
for idx in range(10,-1,-1):
    if idx!=0:
        print(idx,end=' ')
    else:
        print("happynewyear!!")

"""
문제2-3) 양의 두 정수 a,b를 입력 받아, a부터 b까지의
정수의 합을 구하여 출력하는 프로그램을 작성하시오. (for 또는 while을 이용할 것)
단, 조건 a<=b 을 만족하는 값만 고려한다.
Enter two integers:5 10
The sum from 5 to 10 is 45
"""
a=5
b=10
val_sum=0
for idx in range(a,b+1):
    val_sum+=idx
print('a: %d, b: %d, result: %d' %(a,b,val_sum))

"""
문제2-4) 주어진 문자열에 문자a가 몇 개 있는지 구하는
프로그램을 작성하시오.(for문 사용할 것)
"""
word='banana'
word.count('a')
counter=0
for idx in range(len(word)):
    if word[idx]=='a':
        counter+=1
print(counter)


"""
문제2-5) for 문과 range()함수를 이용하여 다음과 같이 출력되도록 작성하시오.
0 1 2 3 4 5 6 7 8 9
0 5 10 15 20 25 30 35 40 45 50
10 9 8 7 6 5 4 3 2 1
"""
for idx in range(10):
    print(idx,end=' ')
for idx in range(0,51,5):
    print(idx,end=' ')
for idx in range(10,0,-1):
    print(idx,end=' ')

"""
문제2-6) for 문을 사용하여 리스트(colors)의 모든 내용을 출력하시오. (단, range()를 이용하지 않는다.)
red
green
blue
"""
colors=["red","green","blue"]
for c in colors:
    print(c)

"""
문제2-7) 리스트 a 전체를 반복해서 방문하되, 짝수만 출력하시오.(for 문 사용)
"""
a=[1,3,4,5,6,7,8,9,10,11,12,13]
[x for x in a if x%2==0]

"""
문제2-8) 구구단 출력1 ­ PPT 문제 출력하고 싶은 단을 입력하세요:7
7*1=7
7*2=14
7*3=21
7*4=28
7*5=35
7*6=42
7*7=49
7*8=56
7*9=63
"""
num=7
for idx in range(1,10):
    print("%d * %d = %d" %(num,idx,num*idx))

"""
문제2-9) 구구단 출력2(중첩 반복문)
"""
for idx0 in range(2,10):
    for idx1 in range(1,10):
        print("%d * %d = %d" %(idx0,idx1,idx0*idx1))

"""
문제2-10) 구구단 출력2(중첩 반복문)
"""
for idx0 in range(2,10):
    for idx1 in range(1,10):
        print("%d * %d = %d" %(idx0,idx1,idx0*idx1), end=' ')
    print('')

"""
문제2-11) 아래와 같은 문장이 주어졌을 때, 아래의 실행 예시처럼 출력되도록 작성하시오.
"""
word1='sally'
word2='goes'
word3='to'
word4='the'
word5='store'
sentense=[word1,word2,word3,word4,word5]
print(' '.join(sentense))

"""
문제2-12) ★ 출력 프로그램 - PPT 문제
"""
x0=3159
for x in str(x0):
    print('*'*int(x))

"""
문제2-13) - PPT 문제
“done“을 입력할 때까지 사용자로부터 숫자를 입력 받아 리스트에 저장하고,
“done“을 입력하면, 리스트의 평균, 최대값과 최소값을 출력하는 프로그램을 작성하시오.
(힌트) sum(),max(),min() 함수를 사용
"""
flag=1
array=list()
while flag:
    x=input('enter a number')
    if x!='Done':
        array.append(int(x))
    else:
        flag=0
print('entered numbers:', array)
print('average: %.2f, max: %.2f, min: %.2f' \
    %(sum(array)/len(array),max(array),min(array)))
