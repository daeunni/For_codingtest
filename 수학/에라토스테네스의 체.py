"""
소수 찾기 
  - 주어진 N개 중에서 소수가 몇개인지 찾아서 출력하기 
  - 에라토스테네스의 체를 이용하는 문제!
  - 배수를 지우는 과정을 언제까지 할 것이며, 어떻게 표현할까?!? 
"""
# 에라토스테네스의 체
def era(n):
  n = max(nums)
  a = [False, False] + [True] * (n-1)
  primes = []
  for i in range(2, n+1):
    if a[i]:
      primes.append(i)
      for j in range(2*i, n+1, i):
        a[j] = False
  return primes
  

if __name__ == '__main__':
  N = int(input())
  nums = list(map(int, input().split()))   # 이 중 소수가 몇개인지 출력하기 
  result = 0 

  n = max(nums)
  primes = era(n)    # 에라토스테네스의 체 시행 

  for i in nums : 
    if i in primes : 
      result += 1
  print(result)
