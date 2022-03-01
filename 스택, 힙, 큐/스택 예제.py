"""

- 스택 : 박스쌓기 (선입후출, 후입선출)
  * 재귀함수의 형태와 유사함 (나중에 들어온 작업이 종료되어야 맨 처음 작업도 종료되므로)
  * append, pop으로 구현

"""
stack = []

stack.append(5)
stack.append(2)
stack.append(3)
stack.append(7)
stack.pop()  # 맨 나중에 들어온 7이 빠진다

stack.append(1)
stack.append(4)
stack.pop()  # 맨 나중에 들어온 4가 빠진다

print(stack)  # [5, 2, 3, 1] : 넣은 순서대로 출력
print(stack[::-1])  # [1, 3, 2, 5] : 나중 원소 순서대로 출력
