"""
Brackets
  - 대칭이어야 nested라고 판단하므로, stack을 이용해 괄호의 대칭을 판단하는 문제!
  - 열린 괄호를 우선 스택에 모두 append하고, 이들을 pop하면서 닫힌 괄호와 비교한다.
  - 예외처리에 신경써야하는 문제다!
"""

def solution(S):

  # 스택으로 구현 
  stack = []

  for i in S : 
    if i == '{':
      stack.append('{')
    elif i == '[':
      stack.append('[')
    elif i == '(':
      stack.append('(')

    # 열린괄호가 모두 append 되었으면 이제 차례로 pop해 닫힌 괄호와 비교할 차례
    else:

      # 예외 1) 닫힌괄호부터 시작해서 pop할게 없을 때 
      if len(stack) == 0 :
        return 0

      p = stack.pop()

      # pop한 것과 다르면 
      if i == '}' and p != '{':
        return 0
      elif i == ']' and p != '[':
        return 0
      elif i == ')' and p != '(':
        return 0

  # 예외 2) 열린 괄호만 두번 들어올 때 방지 
  if len(stack) == 0:
    return 1
  else:
    return 0
