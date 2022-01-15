## 피보나치수열 재귀함수로 구현하기
## >> n == 17 : 17번째까지 피보나치수 구하기

def fibo(n):
    if n == 0:
        return 0

    elif n == 1:
        return 1

    else:
        return fibo(n - 1) + fibo(n - 2)


print(fibo(int(input())))