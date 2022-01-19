"""
DFS 예제 (스택, 재귀함수 이용)
"""

def dfs(graph, v, visited):

  visited[v] = True     # 현재 노드 방문처리
  print(v, end=' ')     # 스택에 넣는 순서 (순회하는 순서)로 출력

  # 현재 노드와 연결된 다른노드 재귀적 방문
  for i in graph[v]:

    # 방문 기록이 없으면 ?
    if not visited[i]:
      dfs(graph, i, visited)     # 여기서부터 다시 dfs 재귀호출

#------------------------------------------------------------------
# ex : 9개의 노드를 가진 graph
graph = [
         [],
         [2,3,8],
         [1,7],
         [1,4,5],
         [3,5],
         [3,4],
         [7],
         [2,6,8],
         [1,7]
]

visited = [False] * 9    # 방문 기록

dfs(graph, 1, visited)