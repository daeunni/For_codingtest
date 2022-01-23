"""
특정 거리의 도시찾기

  - 모든 edge의 weight가 1로 동일하므로** BFS로 최단거리 찾기
  - 특정 시작노드부터 모든 node까지의 최단거리를 BFS로 계산한 후 특정 k의 최단거리를 가지는 노드만 출력

  * 단방향 그래프 나타내기 = 노드별로 2차원리스트를 만든 후 연결리스트를 이용하기

"""
from collections import deque

n, m, k, x = map(int, input().split())  # 노드 개수, edge 개수, 출력할 최단거리, 시작 노드
graph = [[] for _ in range(n + 1)]  # 노드 + 1 개수만큼 2차원리스트로 나타내기 (왜 노드 + 1일까?????)

# 단방향 그래프 edge 정보 입력받기 : 노드별 연결리스트 사용
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)  # 노드별 연결된 엣지가 담긴 리스트 생성

# 노드별 최단거리 저장
dis = [-1] * (n + 1)  # 우선 -1로 모든 노드 초기화해놓기 (-1이면 아직 방문하지 않은 것)
dis[x] = 0  # 시작노드 거리는 0으로 설정

# -------------------------------------
# BFS로 시작노드로부터 각 노드의 최단거리 찾기
# -------------------------------------
q = deque([x])

while q:
    now = q.popleft()  # pop 해서 현재도시로 설정

    # 현재 도시와 연결된 모든노드 확인
    for next in graph[now]:

        # 아직 방문하지 않은 노드라면
        if dis[next] == -1:
            # 최단거리 갱신하기
            dis[next] = dis[now] + 1
            q.append(next)  # q에 넣기

# ----------------------------
# 최단거리가 K인 노드 오름차순 출력
# ----------------------------

check = False

for i in range(1, n + 1):
    if dis[i] == k:
        print(i)
        check = True

if check == False:  # k인 최단거리가 없을 때
    print(-1)