"""
스택 수열 
  - n까지의 숫자를 오름차순으로 넣을 때 적절히 스택에서 push, pop하여 정해진 수열 만들기 
  - 만들 수 없으면 NO를 출력 ! 
  - 혼자 그래도 잘풀었다 이다은 ~~~ 
"""
import sys
input = sys.stdin.readline
n = int(input())
goal = []
for _ in range(n):
  goal.append(int(input()))

st1 = []   # append
st2 = []    # pop한 요소 (최종 출력)
answer = []
r = 0

# goal 요소 하나씩 반복문 
for num in goal : 

  # num까지 우선 st1에 넣어야 하면 
  if r < num and r <= n: 
    for a in range(r+1, num+1):       # 여기가 문제인 듯 
      st1.append(a)       
      answer.append('+')
  
  r = max(r, num)   # 범위설정 변수 r 업데이트 
  b = st1.pop()
  
  if b == num : 
    st2.append(b)
    answer.append('-')

# print 
if goal == st2 : 
  for i in answer : 
    print(i)

else:
  print('NO')
