"""
우선순위 큐를 이용한 다익스트라
  - O(ElogV) 복잡도를 가지며, 최단 거리를 매번 선형탐색하는 것보다 훨씬 빠름
  - 우선순위 큐(최소 힙)에 (거리, 노드) 튜플로 적재되도록 함 (거리가 작은 순으로 출력되도록)
"""

import heapq

INF = int(1e9)

n, m = map(int, input().split())  # 노드, 엣지의 개수 입력받음
start = int(input())  # start node

graph = [[] for i in range(n + 1)]  # 2차원 리스트 (노드별 엣지 정보 적재할 공간)

distance = [INF] * (n + 1)  # 최단거리 테이블 무한으로 초기화

# 모든 엣지 정보 적재
for _ in range(m):
    a, b, c = map(int, input().split())  # a 노드에서 b 노드로 가는 비용이 c라는 의미
    graph[a].append((b, c))  # (도착지점, 비용) 튜플 적재


def dijkstra_heapq(start):
    q = []

    heapq.heappush(q, (0, start))  # start node 거리 자체는 0으로 먼저 힙에 삽입
    distance[start] = 0

    # 큐가 비어있지 않다면
    while q:
        dist, now = heapq.heappop(q)  # 현재 가장 거리가 짧은 노드 꺼내기

        # 만약 이미 처리된 적 있는 노드라면 무시
        if distance[now] < dist:
            continue

        # 아니라면 해당 노드의 edge들 검토
        for i in graph[now]:

            cost = dist + i[1]  # cost 계산

            # 예전 값보다 현재 cost가 작을경우 > 업데이트
            if cost < distance[i[0]]:
                distance[i[0]] = cost  # 업데이트
                heapq.heappush(q, (cost, i[0]))  # 업데이트 하고 이걸 다시 우선순위 큐에 넣는다


# 다익스트라 수행
dijkstra_heapq(start)

# 최단거리 출력
for i in range(1, n + 1):

    if distance[i] == INF:
        print('도착할 수 없음')

    else:
        print(distance[i])
