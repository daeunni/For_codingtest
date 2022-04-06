"""
로또 
  - 집합 중에서 6개를 고르는 모든 경우의 수 출력하기 
  - 조합을 만드는 문제는 <1차원 dfs 탐색>으로 풀면된다! 
"""

def dfs(lotto, s, visited):    # s는 로또 집합 리스트 / lotto에 조합 내 원소 적재 

  # len이 6이면 print 
  if len(lotto) == 6 : 
    for i in range(6):
      print(s[lotto[i]], end=' ')   # S에서 lotto[i]에 해당하는 인덱스 출력 
    print()
    return 

  t_visited = visited[:]

  ## visited 노드 순회 반복문 (i는 0부터 k-1까지 )
  for i in range(len(t_visited)):
    
    if not t_visited[i]:               # 방문하지 않았으면 
      t_visited[i] = True

      print('lotto+i:', lotto + [i])   # 방문하지 않은 

      dfs(lotto + [i], s, t_visited)   # lotto에 계속 unvisited index 적재 
      
      
      
while True : 
  s = list(map(int, input().split()))   # lotto 집합 S를 입력 
  if s[0] == 0 :      # 종료조건 
    break

  s.pop(0)   # 첫 k 원소 제외 
  visited = [False] * len(s)

  dfs([], s, visited)   # 빈 리스트에서 시작 
  print()
