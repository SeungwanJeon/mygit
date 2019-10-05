#과제 1 prime

def check_prime(num):
    for i in range(2,1000):
        if num%i==0:
            return 0

def main():
    a=10
    b=15
    if check_prime(a):
        print(str(a)," 소수")
    else:
        print(str(a)," 소수아님")

if __name__='__main__':
    main()
