"""
요세푸스 문제 
  - 원형 큐를 이용하기 ! (deque로 구현)
"""

from collections import deque
n, k = map(int, input().split())

circle = deque([i+1 for i in range(n)])
index = 0
print('<', end='')

for i in range(n-1): 
  for _ in range(k-1):
    a = circle.popleft()
    circle.append(a)       # 빼서 뒤에넣기.... 
    
    print('popleft : ', a)
    print('circle : ', circle)
  
  print('***' * 10)
  print(f'{circle.popleft()},')   # 가장 왼쪽꺼를 출력... 

print(f'{circle.popleft()}>', end='')
