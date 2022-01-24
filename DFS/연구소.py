"""
연구소
  - 바이러스(2)가 감염되어가는 과정은 dfs(재귀함수)를 이용해 구현한다
    > 바이러스가 "상하좌우"로 이동한다고 생각한다

  - 3개의 벽을 어디에 세울지는 완전탐색으로 해결한다 (모든 경우의 수 찾기)

  - [세로][가로] : 2차원리스트 원소접근 가능 !
"""

n, m = map(int, input().split())
data = []  # 초기 맵 리스트
temp = [[0] * m for _ in range(n)]  # 3개의 벽 설치 뒤 맵 리스트

# 초기 맵 입력받기 (0, 1, 2)
for _ in range(n):
    data.append(list(map(int, input().split())))

# 바이러스가 이동할 상하좌우 4가지 방향 정의
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

result = 0


# ----------------------------------------------
# 1. DFS를 이용해 바이러스를 상하좌우로 퍼지도록 만들기
# ----------------------------------------------

def virus(x, y):  # x, y는 input 좌표

    for i in range(4):  # 상하좌우 이동
        nx = x + dx[i]
        ny = y + dy[i]

        if nx >= 0 and nx < n and ny >= 0 and ny < m:  # 정해진 범위 내에서

            # 감염 가능하면
            if temp[nx][ny] == 0:
                temp[nx][ny] = 2  # 감염시키고

                virus(nx, ny)  # 다시 재귀적으로 수행하기


# -------------------------------------
# 2. 안전지대 계산하기 (그 당시 해당 맵에서)
# -------------------------------------

def get_score():
    score = 0
    for i in range(n):
        for j in range(m):
            if temp[i][j] == 0:  # [세로][가로] > 2차원리스트 원소 접근 가능
                score += 1
    return score


# -------------------------------------------------
# 3. 울타리 설치하며 모든 경우의수를 고려하며 안전영역 계산하기
# -------------------------------------------------

def dfs(count):
    global result

    # 울타리가 3개 모두 설치된 경우
    if count == 3:

        # temp 맵에 각 2차원리스트 element를 복사하기
        for i in range(n):
            for j in range(m):
                temp[i][j] = data[i][j]  # 복사하기

        # 각 위치에서 만약 2라면 바이러스 전파 시작
        for i in range(n):
            for j in range(m):
                if temp[i][j] == 2:
                    virus(i, j)

        # 안전지대 계산하기
        result = max(result, get_score())
        return

        # 빈 공간에 울타리 설치하기 > 이 부분이 왜 무작위로 세 부분을 설치하는 코드가 되는지는 아직 잘 모르겠음.
    for i in range(n):
        for j in range(m):

            if data[i][j] == 0:  # 빈공간이면
                data[i][j] = 1
                count += 1

                dfs(count)

                data[i][j] = 0  # 여기는 무슨 의미인지 잘 모르겠어,,,
                count -= 1


dfs(0)
print(result)