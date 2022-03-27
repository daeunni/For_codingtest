"""
좌표 정렬하기 
"""
import sys
n = int(input())
ax = []

for _ in range(n):
  a, b = map(int, input().split())
  ax.append((a, b))    # 튜플로 적재

new = sorted(ax, key=lambda x : (x[0], x[1]))    # x같으면 y증가하는 순서 
for i in new : 
  print(i[0], i[1])
