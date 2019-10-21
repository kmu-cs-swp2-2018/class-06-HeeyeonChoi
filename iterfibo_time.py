import time

def fibo(n):
    if n <= 1:
        return n
    return  fibo(n-1) + fibo(n-2)

def iterfibo(n):
    if n <= 1 :
        return n
    f_1 = 1
    f_0 = 0
    f_2 = 0
    for i in range(n-1):
        f_2 = f_1 + f_0
        f_0 = f_1
        f_1 = f_2
    return f_2



while True :
    nbr = int(input("Enter a number: "))
    if nbr == -1:
        break
    ts = time.time()
    fibonumber = iterfibo(nbr)
    ts = time.time() - ts
    print("IterFibo(%d)=%d, time %.6f" % (nbr, fibonumber, ts))

    ts = time.time()
    fibonumber = fibo(nbr)
    ts = time.time() -ts
    print("Fibo(%d)=%d, time %.6f" % (nbr, fibonumber, ts))

