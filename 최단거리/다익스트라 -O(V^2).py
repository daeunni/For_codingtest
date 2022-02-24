"""
조금은 느린.. 다익스트라 알고리즘
  - O(V^2)의 복잡도를 가지는 다소 비효율적인 코드 (V = 노드 수)
  - 하나의 start node에서 모든 node까지의 최단거리 구하기
"""

# import sys
# input = sys.stdin.readline       # 그냥 input 함수보다 빠름 ㅎㅎ
INF = int(1e9)  # 10억을 편하게 나타내기

n, m = map(int, input().split())  # 각각 node, edge의 개수
start = int(input())  # start node
graph = [[] for i in range(n + 1)]  # node들 저장

visited = [False] * (n + 1)  # 방문 체크 리스트
distance = [INF] * (n + 1)  # 최단거리 갱신할 리스트 (노드 개수 + 1만큼 만들면 됨)

# edge 정보 입력받기 !!
# >> a번 노드에서 b번 노드로 가는 비용이 c
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))  # node 그래프 자리에 <튜플>로 저장하기


# 1) unvisited node 중에서 가장 최단 거리가 짧은 노드 반환
def get_smallest_node():
    min_val = INF
    index = 0

    # 노드 개수만큼 반복
    for i in range(1, n + 1):

        # unvisited 하고 min_val 보다 작으면 업데이트
        if distance[i] < min_val and not visited[i]:
            min_val = distance[i]
            index = i  # 최소거리 index 반환

    return index


# 2) 다익스트라 구현
def dijkstra(start):
    distance[start] = 0
    visited[start] = True

    # start node와 연결되어 있는 노드 j들
    for j in graph[start]:
        distance[j[0]] = j[1]  # distance 리스트에 갱신

    for i in range(n - 1):
        now = get_smallest_node()  # unvisited 노드 중에서 최단거리 가장 짧은 노드 꺼냄
        visited[now] = True  # 해당 노드 냉큼 방문처리

        for j in graph[now]:
            cost = distance[now] + j[1]  # now의 거리에서 새로운 now의 인접한 노드의 비용 추가하기

            if cost < distance[j[0]]:
                distance[j[0]] = cost  # update


# 함수 실행
dijkstra(start)

# 노드별 start node로부터 최단거리 출력
for i in range(1, n + 1):
    if distance[i] == INF:
        print('도달할 수 없는 노드임')
    else:
        print(distance[i])  # distance에 저장된 값 출력하기