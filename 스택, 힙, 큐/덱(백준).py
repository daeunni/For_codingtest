"""
덱 (deque)
  - 양쪽으로 삽입, 삭제할 수 있는 자료구조라고 생각하면 됨 
  - 큐 처럼 python의 deque 라이브러리를 사용하면 된다 (append, appendleft, pop, popleft)
"""
import sys 
from collections import deque
n = int(sys.stdin.readline())
q = deque()        # 큐와 똑같이 deque를 선언함 

for _ in range(n):
  com = sys.stdin.readline().split()

  if com[0] == 'push_front':
    q.appendleft(com[1])

  elif com[0] == 'push_back':
    q.append(com[1])

  elif com[0] == 'pop_front':
    if len(q) != 0 : print(q.popleft())
    else: print(-1)
  
  elif com[0] == 'pop_back':
    if len(q) != 0 : print(q.pop())
    else: print(-1)

  elif com[0] == 'size':
    print(len(q))

  elif com[0] == 'empty' : 
    if len(q) != 0 : print(0)
    else : print(1)

  elif com[0] == 'front' : 
    if len(q) != 0 : print(q[0])
    else : print(-1)

  else:
    if len(q) != 0 : print(q[-1])
    else : print(-1)
