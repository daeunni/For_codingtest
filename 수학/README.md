# 💌 수학 관련 알고리즘 Idea 정리 
약수, 소수, 최대공약수 등 구하기 !     



## 1. 에라토스테네스의 체
- 소수를 구하는 알고리즘 
- 특정 배수를 지워가는 식으로 전개된다. 

```python
def era(n):   
  """
  Input : 몇까지 탐색할지 
  Output : n까지 숫자 중 소수를 포함한 리스트 
  """
  a = [False, False] + [True] * (n-1)
  
  primes = []
  for i in range(2, n+1):
    if a[i]:
      primes.append(i)
      for j in range(2*i, n+1, i):
        a[j] = False     # 배수를 지운다!
  return primes
```


## 2. 유클리드 호제법 
- 최대공약수, 최소공배수 구하기 
```python
def gcd(n, m):

  """
  Input : 두 수
  Output : 두 수의 최대공약수 
  """
  while m : 
    n, m = m, n%m
  return n
```

