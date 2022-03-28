"""
괄호 
  - 완벽한 대칭 괄호를 골라내는 스택문제
"""
n = int(input())
strings = []
results = []

# input 
for _ in range(n):
  strings.append(input())

for s in strings:
  stack = []
  answer = 0 

  for i in s : 
    if i == '(':
      stack.append(i)   # 열린괄호면 stack에 append 

    else :              # 닫힌괄호 등장하면 pop
      
      # stack이 비어있지 않으면 
      if stack : 
        open = stack.pop()
        if open+i != '()':   # 짝을 이루지 않으면 잘못되었다고 판단 
          answer += 1

      else:
        answer += 1
  
  if len(stack) != 0 : 
    answer += 1
  
  if answer == 0 : results.append('YES')
  else : results.append('NO')

# print 
for i in results:
  print(i)
