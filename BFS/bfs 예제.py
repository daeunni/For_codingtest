"""
BFS 예제 (큐 이용)
"""

from collections import deque

def bfs(graph, start, visited):

  q = deque([start])
  visited[start] = True    # 현재 시작 노드 방문 처리

  ## 큐가 빌때까지 반복하기
  while queue:

    # 큐에서 가장 예전에 들어온 원소 하나 뽑기
    v = q.popleft()
    print(v, end=" ")

    # v의 인접 노드 순회
    for i in graph[v]:

      # 방문하지 않은 노드는 큐에 append
      if not visited[i]:
        q.append(i)
        visited[i] = True