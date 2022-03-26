"""
에디터
  - 스택으로 구현해보기 (선입후출) > pop(i)와 insert(i)가 아니라 pop()과 append(v)를 이용할 것 !
  - 커서를 중심으로 스택을 2개로 나눈다. 
"""

# 스택 2개로 시작 
st1 = list(input())
st2 = []
n = int(input())

for _ in range(n):
  com = input().split()

  if com[0] == 'L':
    if st1 :           # st1 비어있지 않으면 (예외처리 이렇게 간단하게 가능...)
      st2.append(st1.pop())
  
  elif com[0] == 'D':
    if st2:
      st1.append(st2.pop())

  elif com[0] == 'B':
    if st1:
      st1.pop()

  else:
    st1.append(com[1])

  print('st1 : ', st1)
  print('st2 : ', st2)

st1.extend(reversed(st2))    # 두 stack을 합쳐준다 
print(''.join(st1))
