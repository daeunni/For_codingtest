"""
수 정렬하기2
"""
import sys    # 빠른 입출력을 위해 

n = int(sys.stdin.readline())
numbers = []

for _ in range(n):
  numbers.append(int(sys.stdin.readline()))

# 이거보다 훨씬 빠르다! 
# for _ in range(n):
#   numbers.append(int(input()))

numbers.sort()    # python의 기본 정렬은 팀정렬을 사용한다(꽤 효율적)

for i in numbers:
  print(i)
