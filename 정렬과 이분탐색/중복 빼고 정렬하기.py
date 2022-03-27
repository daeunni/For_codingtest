"""
중복 빼고 정렬하기 
"""
import sys
# input = sys.stdin.readline
n = int(input())
nums = list(map(int, input().split()))
new = sorted(set(nums))
for i in new:
  print(i, end=' ')
