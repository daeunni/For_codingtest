"""
미로탈출

  - 최단거리 = BFS (큐) 이용 !!
  - 특정 위치로만 움직이는 최단거리 구하기
"""
from collections import deque  # deque 자료구조 이용

n, m = map(int, input().split())  # n*m size

graph = []

# graph = 2차원 리스트로 나타내기
for i in range(n):
    graph.append(list(map(int, input())))  # 여기는 split이 필요 없다 !!

# 상하좌우 정의
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def dfs(x, y):
    q = deque()
    q.append((x, y))

    # 큐가 빌 때까지 반복
    while queue:
        x, y = queue.popleft()  # queue에서 빼기

        # 현재 위치에서 상하좌우 네 방향으로 확인
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # 미로 공간 벗어난 경우 무시
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue

            # 괴물이 나오는 0인 경우 무시하기
            if graph[nx][ny] == 0:
                continue

            # 괴물이 없는 해당 노드를 처음 방문하는 경우에만 최단거리 기록
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                q.append((nx, ny))  # 여기서부터 큐에 넣어 또 다시 시작

    return graph[n - 1][m - 1]  # 가장 오른 쪽 아래 최단거리 반환


print(bfs(0, 0))