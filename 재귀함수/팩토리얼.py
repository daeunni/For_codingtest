# 재귀함수로 팩토리얼 구현하기
## >> 재귀함수는 반드시 탈출조건이 필요하다 !!

a = int(input())

def fac(n):
  if n == 0 :
    return 1
  else :
    return n * fac(n-1)

print(fac(a))