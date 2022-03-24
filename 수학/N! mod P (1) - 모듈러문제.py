"""
N! mod P (1)
  - N!을 P로 나눈 나머지 구하기 (P는 소수)
  - 전형적인 모듈러의 연산 문제인 것을 오늘 알았다.. 
"""

n, p = map(int, input().split())
ans = 1
for i in range(2, n+1):
  ans = (ans * i) % p       # 음... 이게 왜 이렇게 되는지 아직은 모르겠져.... 

print(ans)
