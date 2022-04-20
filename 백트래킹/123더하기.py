"""
1, 2, 3 더하기 
  - n을 1, 2, 3의 합으로 나타내는 방법의 수 
  - 1, 2, 3으로 이루어진 그래프에서 깊이가 n인 dfs를 수행하는 과정이라고 생각(visited 체크는 안함) 
"""
def dfs(cur_sum, n):
  global count 

  # cur_sum이 n과 같으면 count+1 하고 재귀 중단 
  if cur_sum == n : 
    count += 1
    return
  
  # cur_sum이 n보다 크면 바로 재귀 중단 
  elif cur_sum > n :    
    return

  else : 
    for i in range(1, 4):
      cur_sum += i      # 다음 depth의 노드로 뻗는 부분 
      dfs(cur_sum, n)
      cur_sum -= i      # 이전 depth의 노드로 다시 되돌아가는 역할을 하는 부분

t = int(input())
for _ in range(t):
  n = int(input())    
  count = 0 
  dfs(0, n)
  print(count)
