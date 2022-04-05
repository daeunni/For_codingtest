"""
로또 
  - 집합 중에서 6개를 고르는 모든 경우의 수 출력하기 
"""
import sys
from itertools import combinations 
cases = []

# input 
while True:
  test = list(map(int, input().split()))
  if test[0] == 0 :   # 종료 조건 
    break
  test.pop(0)
  cases.append(test)

# main
for s in cases : 
  com = list(combinations(s, 6))   # 시간복잡도가 괜찮을 지는 모르겠다..ㅠㅁㅠ
  for i in com : 
    print(i[0], i[1], i[2], i[3], i[4], i[5])
  print()
