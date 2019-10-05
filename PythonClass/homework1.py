"""
실습1-1)
a,b 에 각각 5,8을 할당하고 곱셈을 한 값을 result에 저장하여 출력하는 프로그램 작성하기
"""
def mult(a,b):
    return a*b
result=mult(5,8)
print(result)


"""
실습1-2)
x,y 에 각각 10,20을 할당한 후, 다른 변수 z를 이용하여 두 수를 교환하는 프로그램 작성하기
(단, x,y에 숫자를 할당한 후에는 숫자를 직접 이용하지 않는다.)
"""
def swap(x,y):
    z=x
    x=y
    y=z
    return x,y
x=10
y=20
x,y=swap(x,y)
print(x,y)


"""
실습2-1)아래의 코드가 정상적으로 동작하도록 수정하시오. 에러메시지 확인 후, 수정하시오.
print ("수학 점수는 "+90 +"점 이다.") #에러있음
"""
print("수학 점수는 "+str(90)+"점 이다.")


"""
4. 연습문제 HW1.ipynb
(문제 1) PPT(실습 문제1)
화씨온도(℉)를 입력 받아서 섭씨온도(℃)로 바꾸는 프로그램을 작성하시오. (밑줄은 사용자 입력)
"""
F=float(input("enter input"))
C=(F-32)*5/9
print("화씨: %.2f\n 섭씨: %f" %(F,C))

"""
(문제 2) 자동 판매기 프로그램 - PPT(실습문제2)
사용자로부터 투입한 돈과 물건 값을 입력 받아, 잔돈을 계산하여 출력한다. 단, 동전의 개수는 최소화 할 것
(가정)
- 물건 값은 100원 단위
- 자판기의 동전은 500원, 100원만 있음
"""
def f1(x):
    coin500=x//500
    coin100=(x%500)//100
    return coin500, coin100
coin500,coin100=f1(2300)
print("coin500: %dea, coin100: %dea"%(coin500,coin100))

"""
(문제 3) 원의 반지름을 r을 입력 받아, 원의 둘레와 넓이를 구하는 프로그램을 작성하시오.
"""
def circ(r):
    result1=r*2*3.14
    result2=r**2*3.14
    return result1,result2
circ(5)
print("둘레: %.2f, 넓이: %.2f"%circ(5))

"""
(문제 4) 한 문장을 입력 받아, 아래와 같이 각 알파벳 각문자를 원소로 갖는 리스트를 작성하시오.
(문장중에 !,.? ­를 제외한 문자의 입력은 고려하지 않는다.)
"""
x='Python is fun!'
'spliter'.join(x).split('spliter')

"""
(문제 5) 2개의 정수를 입력 받아, 사칙연산 및 나머지 연산의 결과를 아래와 같이 출력하는 프로그램을 작성하시오.
"""
a,b=map(int,input("enter 'a b'").split())
print('%d + %d = %.2f' %(a,b,a+b))
print('%d - %d = %.2f' %(a,b,a-b))
print('%d * %d = %.2f' %(a,b,a*b))
print('%d / %d = %.2f' %(a,b,a/b))


"""
(문제 6) 두 정수를 입력 받아, 합과 평균을 구하여 출력하는 프로그램을 작성하시오.
(평균 소수 첫째 자리까지 나타내기)
"""
a,b=map(int,input("enter 'a b'").split())
print('the sum of %d and %d is %d' %(a,b,a+b))
print('the average of %d and %d is %.1f' %(a,b,(a+b)/2))


"""
(문제 7) PPT(실습문제2)
아래의 실행예제를 참고하여 프로그램을 작성하라. 날짜(연/월/일)입력:2019/08/12
입력한 날짜의 10년 후는 2029년 8월 12일
"""
date=input('날짜입력 yyyy/mm/dd')
y,m,d=(map(int,date.split('/')))
print('10년 뒤는 %d년 %d월 %d일'%(y+10,m,d))



"""
실습6-1)1부터 10까지의 리스트 생성
"""
list(range(1,11))

"""
실습2)10부터 1까지의 리스트 생성
"""
list(range(10,0,-1))

"""
실습3)1부터 10까지의 짝수 리스트 생성
"""
even_list=list(range(2,11,2))
even_list
"""
실습4)1부터 10까지의 홀수 리스트 생성
"""
odd_list=list(range(1,11,2))
odd_list
"""
실습5) 리스트 더하기
"""
even_list+odd_list
