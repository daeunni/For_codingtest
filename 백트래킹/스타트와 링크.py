"""
스타트와 링크 
  - 뭘 dfs의 노드로 넣어야하는지 모르겠어... 뭐에 방문 체크를 해야하지,,,,
"""


def dfs(depth, col_idx):     # depth == raw_idx
  global result

  # 팀 빌딩이 완료되었을 때 
  if depth == N // 2 : 
    start, link = 0, 0

    # 각 노드를 2차원 좌표 (i, j)로 보고 각각을 순회 
    for i in range(N):
      for j in range(N):
        if visited[i] and visited[j]:
          start += mat[i][j]
        
        elif not visited[i] and not visited[j]:
          link += mat[i][j]

    result = min(result, abs(start-link))
    return 

  for i in range(col_idx, N):
    if not visited[i]:
      visited[i] = True
      dfs(depth + 1, col_idx + 1)
      visited[i] = False            # 백트래킹 


if __name__ == '__main__':
  N = int(input())
  mat = []                # 2차원 리스트로 능력치 행렬 적재 
  for _ in range(N):     
    mat.append(list(map(int, input().split())))

  team = [0] * N          # 인덱스 : raw / 값 : raw의 몇번째 값인지 저장 
  visited = [False] * N
  result = 99999999999    # 최솟값 저장 
  dfs(0, 0)
  print(result)
