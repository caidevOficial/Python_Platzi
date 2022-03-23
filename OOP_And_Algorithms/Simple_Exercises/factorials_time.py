import time,sys

def factorial(n):
    response = 1

    while n > 1:
        response *= n
        n -= 1
    # print(response)
    return response


def factorialRec(n):
    if n == 1:
        return n
    else:
        return (n*factorial(n-1))


if __name__ == '__main__':
    number = 150000
    #print(sys.getrecursionlimit())
    
    start = time.time()
    r1 = factorial(number)
    final = time.time()
    print(final-start)

    print('=============')
    start = time.time()
    r2 = factorialRec(number)
    final = time.time()
    print(final-start)
