"""
CountFactors
  - factor의 개수는 약수의 개수와 같다! (약수의 개수를 효율적으로 구하는 문제!)
  - O(N)의 복잡도가 아니라 O(sqrt(N))의 복잡도로 구해야하는 문제 !
"""

# O(N) 복잡도 
def slow_solution(N):
  count = 0 

  # 모든 수를 탐색하게 되는게 문제다!
  for i in range(1, N+1):
    if N % i == 0 :
      count += 1

  return count

# O(sqrt(N)) 복잡도 : 루트 N까지의 수만 탐색하기 
import math 
def solution(N):
  sn = math.sqrt(N)
  result = 0
  i = 1

  # 루트 N까지만 탐색 
  while i <= sn:

    # 예외) 중간에 있는 수 처리 > 약수의 개수가 홀수일 때 중간에 있는 수는 제곱수이다 
    if i**2 == N:
      result += 1
    
    elif N % i == 0:
      result += 2     # 짝꿍꺼까지 더해주기
    
    i += 1 

  return result
