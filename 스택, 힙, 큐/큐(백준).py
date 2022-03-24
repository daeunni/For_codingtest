"""
큐 (Queue)
  - 선입선출의 구조 
  - python에서는 deque 라이브러리로 구현됨 (append, popleft)
"""

from collections import deque
import sys 

n = int(sys.stdin.readline())   # 명령의 수 
q = deque()

for _ in range(n):
  com = sys.stdin.readline().split()

  if com[0] == 'push':
    q.append(com[1])

  elif com[0] == 'pop':
    if len(q) != 0 : print(q.popleft())
    else : print(-1) 
  
  elif com[0] == 'size':
    print(len(q))

  elif com[0] == 'empty':
    if len(q) != 0 : print(0)
    else : print(1)

  elif com[0] == 'front' :    # 큐의 가장 앞에있는 (먼저들어온) 정수 출력 
    if len(q) != 0 : print(q[0])
    else : print(-1)

  else : 
    if len(q) != 0 : print(q[-1])
    else : print(-1)
      
