"""
섬의 개수
  - 음료수 얼려먹기랑 비슷 !! 1(땅)이 연결된 영역 개수 출력하기 \
  - 단 상하좌우 뿐 아니라 **대각선**으로 연결된 지점도 연결되었다고 가정 !!!!!!
  - Input이 연속해서 들어오는 유형
"""

def dfs(x, y):
    if x < 0 or y < 0 or x >= h or y >= w:
        return False

    if graph[x][y] == 0:
        return False

    if graph[x][y] == 1:
        graph[x][y] = 0
        dfs(x - 1, y - 1)
        dfs(x - 1, y)
        dfs(x - 1, y + 1)
        dfs(x, y + 1)
        dfs(x + 1, y + 1)
        dfs(x + 1, y)
        dfs(x + 1, y - 1)
        dfs(x, y - 1)
        return True

    return False



while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break

    graph = []
    for _ in range(h):
        graph.append(list(map(int, input().split())))

    count = 0
    for i in range(h):
        for j in range(w):
            if dfs(i, j) == True:
                count += 1

    print(count)