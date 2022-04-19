"""
1, 2, 3 더하기 
  - n을 1, 2, 3의 합으로 나타내는 방법의 수 
  - 1, 2, 3으로 이루어진 그래프에서 깊이가 n인 dfs를 수행하는 과정이라고 생각(visited 체크는 안함) 
"""
import sys
# input = sys.stdin.readline()
t = int(input())

# dfs 
def num_dfs(n, sub_sum):
  global count 
  if sub_sum > n : 
    return

  if sub_sum == n : 
    count += 1
    return 

  for i in range(1, 4):
    sub_sum += i 
    num_dfs(n, sub_sum)
    sub_sum -= i     

for _ in range(t):
  n = int(input())
  count = 0 
  num_dfs(n, 0)
  print(count)
