"""
바이러스
  - BFS, DFS를 둘 다 이용해도 가능하다 (시작노드는 항상 1)
  - 처음에 그래프 저장방식을 단방향 2차원리스트로 저장했는데, 오류가 났음. (인접행렬로 저장해야함!)
  - 특이하게 DFS + visited check 하는 방법 사용
"""

n=int(input())
m=int(input())

count =0
connect=[[0]*(n+1) for _ in range(n+1)]     # 인접행렬로 그래프 저장하기 !
visited=[False]*(n+1)

# 인접행렬로 저장하는 법
for i in range(m):
    a,b=map(int,input().split())
    connect[a][b]=1
    connect[b][a]=1

# v 노드에 대한 dfs
def dfs(v):
    visited[v]=True
    for i in range(1,n+1):
        if not visited[i] and connect[v][i]:
            global count
            count=count+1
            dfs(i)
dfs(1)
print(count)
