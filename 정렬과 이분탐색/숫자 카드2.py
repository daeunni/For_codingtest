"""
숫자 카드2
  - 1과 다른점은 단순 가지고 있는지 여부가 아니라 몇개를 가지고 있는지 출력해야함 
"""
import sys
from collections import Counter
# input = sys.stdin.readline
n = int(input())
cards = list(map(int, input().split()))
m = int(input())
have = list(map(int, input().split()))   # 얘네를 몇개 가지고있는지 출력해야 함 
 
c = dict(Counter(cards))     # counter 이용 
for i in have : 
  try: print(c[i], end=' ')
  except: print(0, end=' ')
