"""
경쟁적 전염
  - 번호가 낮은 바이러스부터 상,하,좌,우로 먼저 증식 > 큐에 삽입할 때 "정렬"해서 삽입하기!
  - BFS를 이용해야하는 문제 !
  - 특이하게 큐에 삽입하는 자료형을 (종류, 시간, 위치X, 위치Y) 로 설정한다 !
"""
from collections import deque

n, k = map(int, input().split())  # k = 바이러스 수

graph = []  # 전체 맵
data = []  # 바이러스 정보 담는 리스트

# map 입력 받기
for i in range(n):
    graph.append(list(int, input().split()))

    for j in range(n):

        # 바이러스가 존재하는 경우
        if graph[i][j] != 0:
            data.append((graph[i][j], 0, i, j))  # (종류, 시간, 위치X, 위치Y) 저장

# 특정 시간, 위치 입력
target_s, x, y = map(int, input().split())

# 상하좌우 위치
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

## 큐에 삽입할 때 정렬해서 삽입!
data.sort()
q = deque(data)  # 리스트를 deque에 삽입함

# BFS
while q:
    virus, s, x, y = q.popleft()  # 큐에서 꺼내는 원소 구성요소

    if s == target_s:
        break

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx and nx < n and 0 <= ny and ny < n:

            # 감염되기 전이면 바이러스 넣기
            if graph[nx][ny] == 0:
                graph[nx][ny] = virus
                q.append((virus, s + 1, nx, ny))  # 큐에 넣는 자료형 형태로 넣어주기 !

print(graph[x - 1][y - 1])
