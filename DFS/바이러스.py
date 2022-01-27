"""
바이러스
  - BFS를 이용하는 것 같아 (시작노드는 항상 1)
"""
from collections import deque

c = int(input())     # 컴퓨터 수
pair = int(input())  # 연결된 쌍의 수
result = 0


# 연결된 쌍의 수 단방향그래프처럼 저장 >>>> (그래프 입력 방식을 바꿔야할 것 같다. 9, 1같은 경우 현재 count를 못하고 있음)
# >>> matrix 형태로 바꿔보기

graph = [[] for _ in range(c + 1)]
for _ in range(pair):
  a, b = map(int, input().split())    # a > b
  graph[a].append(b)                        # 연결리스트 형태로 저장

  # 그냥 반대도 고려해주면 안되냐 이렇게
  graph[b].append(a)


## BFS로 1과 인접한 쌍 찾기
q = deque([1])            # 시작노드 = 1

# 방문여부 확인
visited = [False for i in range(c+1)]

while q :
  now = q.popleft()
  # print(now)
  result += 1
  visited[now-1] = True

  # 인접노드 탐방
  for next in graph[now]:
    if visited[next-1] == False :
      q.append(next)
      visited[next-1] == True       # 방문체크

print(result-1)