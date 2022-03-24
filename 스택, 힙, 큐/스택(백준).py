"""
스택 (stack)
  - 상자쌓기 (선입후출)의 구조이다!
  - python에서는 리스트로 구현된다 
"""
import sys

N = int(sys.stdin.readline())   # 명령의 수 
stack = []    # 리스트로 stack 구현하기 

for _ in range(N):
  com = sys.stdin.readline().split()

  if com[0] == 'push':
    stack.append(com[1])
  
  elif com[0] == 'pop':
    if len(stack) != 0 : 
      print(stack.pop())
    else:
      print(-1)
  
  elif com[0] == 'size':
    print(len(stack))
  
  elif com[0] == 'empty' : 
    if len(stack) == 0 : 
      print(1)
    else : print(0)

  else : 
    if len(stack) != 0 : 
      print(stack[-1])
    else: print(-1)
