"""
최대공약수와 최소공배수
  - 유클리드 호제법(최대공약수) 이용하기!
"""
n, m = map(int, input().split())

def gcd(n, m):

  """
  Input : 두 수
  Output : 두 수의 최대공약수 
  """
  while m : 
    n, m = m, n%m
  return n

if __name__ == '__main__':
  a = gcd(n, m)                    # 최대공약수 
  b = a * (n // a) * (m // a)      # 최소공배수 
  print(a)
  print(b)
