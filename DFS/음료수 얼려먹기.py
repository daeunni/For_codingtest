"""
< 음료수 얼려먹기 >

- 얼음틀의 형태를 그래프로 어떻게 나타낼까?
- DFS를 이용!
"""

n, m = map(int, input().split())       # 세로 * 가로

# 2차원그래프로 맵 입력받기
graph = []

for i in range(n):
  graph.append(list(map(int, input())))     # 세로줄 개수만큼

def dfs(x, y):

  # 영역을 벗어나면 종료하기 (재귀함수 종료)
  if x <= -1 or x >= n or y <= -1 or y >= m :
    return False

  # 현재 노드를 방문하지 않았다면
  if graph[x][y] == 0 :
    graph[x][y] = 1        # 방문 처리

    ## 이어져있는 상하좌우 위치 재귀적 호출
    dfs(x-1, y)
    dfs(x, y-1)
    dfs(x+1, y)
    dfs(x, y+1)
    return True       # >> 이어져있는 쌍을 찾은 것 ! 우리는 True만 count하면 된다

  return False

## 0으로 이어진 부분 count
result = 0

for i in range(n):
  for j in range(m):

    if dfs(i, j) == True:
      result += 1

print(result)