class Car:
    count=0
    def __init__(self,color='red'):
        self.color=color
        Car.count+=1
        self.count+=1
    def __del__(self):
        Car.count-=1

mycar=Car('red')
print(Car.count)
print(mycar.count)
mycar1=Car('red')
print(Car.count)
print(mycar.count)

id(Car.count)
id(mycar.count)

mycar1=Car()
mycar1.color
print(Car.count)
print(mycar.count)



class myClass1(object):
    def __init__(self, *args, **kwargs):
        #args -- 이름이 없는 인자를 저장하는 tuple
        # #kwargs -- 이름이 있는 인자를 저장하는 dict
        print ("aargs:", args)
        print ("kwargs:", kwargs)
        mynum = 3 if kwargs['num'] is None else kwargs['num']

o = myClass1(3, "hello", num = 1, mystring = "mystring")




class Person:
    name='hong kil dong'
    _age=15
    __address='abc'

    def printinfo1(self):
        print('name:',self.name)
        print('age:',self._age)
        print('address:',self.__address)
    def printinfo2(self):
        print('name:',self.name)
        print('age:',self._age)
        print('address:',self.__address)
    def printinfo3(self):
        print('name:',self.name)
        print('age:',self._age)
        print('address:',self.__address)
print(Person.name)
print(Person._age)
print(Person.__address)
#address는 에러남

p1=Person()
p1.printinfo1()
print(p1.name)
print(p1._age)
print(p1.__address)
#address는 에러남



print('a',2)


# assert에 false 걸리면 프로그램 종료
assert 1>0
print(123)


class Account:
# 계좌의 속성 (Attribute)
    num_acc=0
    def __init__(self, num='OOOO-OOO-OOOOOO',amnt=0,rate=1.0):
        self.num = num
        self.balance = amnt
        self.rate = rate
        Account.num_acc+=1
    # 계좌의 기능 (Method)
    def __add__(self, another):
        new_acc=Account(amnt=self.balance+another.balance,rate=self.rate)
        return new_acc
    def __repr__(self):
        return str(self.balance)
    def deposit(self, money): #입금
        self.balance += money
    def withdraw(self, money):  #인출
        self.balance -= money
        return True
    def obtain_interest (self): #이자 획득
        self.balance += self.balance*(self.rate/100)
    def transfer(self, another, amnt):
        if self.withdraw(amnt):
            another.deposit(amnt)
acc1=Account()
print(acc1)
acc2=Account()
acc3=Account()
acc1.deposit(500)
acc2.deposit(1000)
print(acc1)
print(acc1.balance)
print(acc2.balance)
print(acc3.balance)
acc4=acc1+acc2
acc4=acc1.__add__(acc2)
print(acc4.balance)

acc5=MinBalanceAccount(amnt=500)
acc5.transfer(acc2,500)

print(acc5.balance)
print(acc2.balance)

class MinBalanceAccount(Account):
    def __init__(self, min_balance=0, num='0000-000-000000',amnt=0,rate=0,brate=1.0):
        Account.__init__(self, num=num,amnt=amnt,rate=rate)
        self.min_balance=min_balance
        self.bounus_rate=brate
    def withdraw(self, amnt):
        if self.balance-amnt<self.min_balance:
            print('sorry, minimum balance must be maintained')
            return False
        else:
            return Account.withdraw(self,amnt)
    def obtain_interest(self):
        self.balance+=(self.balance)*((self.rate+self.bounus_rate)/100)
acc4=MinBalanceAccount()


list(range(0,5,2))
