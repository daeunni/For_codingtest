"""
소수 구하기 
  - M이상 N이하의 소수를 모두 출력하는 프로그램 작성하기
"""
# 에라토스테네스의 체
def era(n):
  a = [False, False] + [True] * (n-1)
  primes = []
  for i in range(2, n+1):
    if a[i]:
      primes.append(i)
      for j in range(2*i, n+1, i):
        a[j] = False
  return primes
  

if __name__ == '__main__':
  m, n = map(int, input().split())   # m 이상 n 이하 
  primes = era(n)
  result = [x for x in primes if (m <= x <= n)]   # 리스트 필터링 
  for i in result : 
    print(i)
