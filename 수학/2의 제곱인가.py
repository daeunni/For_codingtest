"""
2의 제곱인가? 
  - 2의 제곱수 찾기 
"""
import math 
n = int(input())

# 어차피 30개밖에 안되므로 1부터 2**30까지 리스트에 저장한다.. (음 더 빠르게 풀 수 있을 것 같은데..)
two = [2**n for n in range(31)]

if n in two : 
  print(1)
else:
  print(0)
