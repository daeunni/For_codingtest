# Awesome graph algorithms templates! 🌟
## [0] Inputs 
- General input format using coding test 
```python
nodes = input().split()
num_nodes = len(districts)
adj_matrix = []
for _ in range(num_districts):   # 2D lists
    adj_matrix.append(list(map(int, input().split())))
```
- When you want to change input 2 dictionary graph format 
```python
def inputs2dicts(starts, ends, node_names) : 
  graphs = {}
  for key in node_names : 
    values = []
    for i, k in enumerate(starts) : 
      if k == key : 
        values.append(ends[i])
    graphs[key] = values
  return graphs 
```


## [1] 그래프 순회 
### BFS
- 큐 이용  
```python
""" BFS """ 
def bfs(dict_graph, start) : 
  visit = [start] ; queue = [start]
  
  while len(queue) > 0 : 
    for adj_node in dict_graph[queue[0]] : 
      if adj_node not in visit :            # 아직 방문 X  
        visit.append(adj_node)
        queue.append(adj_node)
    del queue[0]    # 인접 노드 모두 탐색했으면 dequeue

  return visit      # 순회 순서 리턴 
```

### DFS
- 재귀함수 이용 
```python
""" DFS """ 
visit = []
def dfs(dict_graph, start) :  
  visit.append(start)
  for adj_node in dict_graph[start] : 
    if adj_node not in visit : 
      dfs(dict_graph, adj_node)    # 재귀함수 
```


## [2] 그래프 정렬 
### 위상정렬 
- 순서에 맞게 그래프 방문
- 진입차수가 0인 node & edge를 차례로 제거 
```python
""" 위상정렬 """
def topo_sort(dict_graph) : 
  while len(dict_graph) > 0 : 
    for i in dict_graph.keys() : 
      input_zero = True            # 진입차수 0인지 체크 

      for check in dict_graph.keys() :   
        if i in dict_graph[check] :      # i로의 진입 차수가 존재하면 
          input_zero = False 
        
      if input_zero : 
        print(i)
        del dict_graph[i]     # 진입차수 0인 node + edge는 삭제 
        break                 # 즉시 반복문 중단 
```


## [3] MST - 최소 신장 트리 
> Weighted-graph에 존재하는 모든 노드를 최소비용으로 연결 

### Prim
- 임의의 최소 노드 선택 후 적은 비용으로 이을 수 있는 노드 선택 
- MeanHeap + 우선순위 큐로 구현 > `O(ElogV^2)`
- Greedy 

```python
""" MST 찾기 (1) Prim """
from heapq import heappush, heappop     # Meanheap(pop하면 최소 원소 반환) + 우선순위 큐 이용 > O(ElogV**2)

def Prim(adj_matrix, node_names, start) : 
  """
  adj_matirx = 2d lists 
  node_names = ['A', 'B', ..]
  """
  h = []
  connect = [False for i in range(len(node_names))]   # 노드별 연결 여부 판단 
  total_weight = 0 
  node_count = 0     # 모든 노드 연결되면 중단하기 

  heappush(h, (0, start))   # (weight, node)로 삽입 

  while node_count < len(node_names) : 
    min_w_node = heappop(h)         # Meanheap 구조로 min 값(=root 값)이 pop된다. 
    pop_weight, pop_node = min_w_node[0], min_w_node[1]   

    if not connect[pop_node] :      # pop된 노드가 미연결 노드이면 
      connect[pop_node] = True 
      total_weight += pop_weight    # weight, count update 
      node_count += 1 

      for i in range(len(node_names)) : 
        if adj_matrix[pop_node][i] != 0 and connect[i] == False :     # 인접한 노드 중 미연결 노드이면 push 
          heappush(h, (adj_matrix[pop_node][i], i)) 
```

### Kruskal
- 가중치 낮은 edge 부터 고려 + cycle 생기지 않도록 
- cycle 여부는 dictionary로 판단 

```python
""" MST 찾기 (2) Kruskal """
def Kruskal(edges, node_names) : 
  """
  edges = [ (weight, A, B), (weight, A, C)...]
  node_names = ['A', 'B', ..]
  """
  edge_count = 0 ; total_weight = 0 

  union = dict()           # cycle 체크 용 딕셔너리 (value에 같은 팀 저장)
  for n in node_names : 
    union[n] = n

  edges.sort()    # 오름차순 정렬 > 정렬 후라서 반복문만 돌면 됨 
  for ed in edges : 
    if union[ed[1]] != union[ed[2]] :      # edge 출발, 도착지점이 다른 팀이면 (=다른 value이면)
      total_weight += ed[0]
      edge_count += 1

    for n in node_names : 
      if union[n] == union[ed[2]] :        # 도착지 팀이었다면 > 출발지 팀과 합쳐주는 작업 (하나의 거대한 군집 만들기)
        union[n] = union[ed[1]]

    if edge_count >= len(node_names) -1 :  # 종료 조건 
      break 
```


## [4] 최단거리 
### Dijkstra 
- Weight가 모두 양수일 때 + 시작점 정해져 있을 때 
- Prim과 비슷 
- Greedy 

```python
""" 최단거리 (1) Dijkstra """
from heapq import heappush, heappop    # MinHeap (=Prim)

def Dijkstra(adj_matrix, node_names, start) : 
  h = []
  connect = [False for i in range(len(node_names))]
  heappush(h, (0, start))

  while len(h) > 0 :  
    min_w_node = heappop(h)     # 최소 가중치를 가지는 노드 pop 
    pop_weight, pop_node = min_w_node[0], min_w_node[1]   
    if not connect[pop_node] : 
      connect[pop_node] = True 

      # 인접한 노드 
      for i in range(len(node_names)) : 
        if adj_matrix[pop_node][i] != 0 and connect[i] == False :    # 인접 노드 중 미연결인 노드 
          heappush(h, (pop_weight + adj_matrix[pop_node][i], i))     # 최단거리 업데이트해 push 
```

### Bellman-Ford
- Weight 음수 가능 + 시작점 고정 
- (node 수 - 1) round 까지만 고려하면 됨 

```python
""" 최단거리 (2) Bellman-Ford """
def BellmanFord(adj_matrix, node_names, start) : 
  min_weight = [float('inf') for i in range(len(node_names))]
  min_weight[start] = 0 
  on_node = [start]         # 인접했던 노드들 (스쳐 지나갔던 노드들) 삽입 
  new_on_node = []

  for round in range(len(node_names)-1) :       # 노드수 - 1 round 까지만 돌면 최단거리 확정됨 
    for adj_node in on_node :                   # 인접했었던 노드들에 대해 고려 
      for i in range(len(node_names)) :         # 전체 노드에 대해 고려 
        if adj_matrix[adj_node][i] != 0 :       # 연결되어 있으면 
          new_weight = min_weight[adj_node] + adj_matrix[adj_node][i]
          min_weight[i] = min(min_weight[i], new_weight)    # 최솟값으로 업데이트 
          new_on_node.append(i)

    on_node = new_on_node
    new_on_node = []

  print(min_weight)      # 최종적으로 모든 최단거리 확정 
```

### Floyd-Warshall
- 시작점 고정 X 
- 경유지를 고려하는 방법 `O(V^3)`

```python
""" 최단거리 (3) Floyd-Warshall """
def FloydWarShall(adj_matrix, node_names) : 

  for i in range(len(adj_matrix)) : 
    for j in range(len(adj_matrix)) : 
      if i!=j and adj_matrix[i][j] == 0 :       # 연결되어있지 않으면 
        adj_matrix[i][j] = float('inf')         # 혼동을 막기 위해 inf로 설정 

  for mid in range(len(adj_matrix)) :           # 경유지 고려 
    for start in range(len(adj_matrix)) : 
      for end in range(len(adj_matrix)) : 
        new_weight = adj_matrix[start][mid] + adj_matrix[mid][end]        # 경유지 거칠 때 weight 
        adj_matrix[start][end] = min(new_weight, adj_matrix[start][end])  # 최솟값 비교 
```
