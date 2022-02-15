"""
정수 삼각형
  - DP 테이블에 삼각형을 저장하고, 이를 최댓값으로 갱신하는 방식
  -

"""

# 삼각형 크기
n = int(input())
dp = []

for _ in range(n):
  dp.append(list(map(int, input().split())))     # 바로 dp 테이블에 삼각형 담고 해당 원소까지 최댓값 갱신

for i in range(1, n):
  for j in range(i+1):

    # 왼쪽 위에서 내려오는 경우
    if j == 0 :
      up_left = 0               # 리스트 범위 벗어나는 부분

    else:
      up_left = dp[i-1][j-1]

    # 바로 위에서 내려오는 경우
    if j == i :
      up = 0                   # 리스트 범위 벗어나는 부분

    else:
      up = dp[i-1][j]

    # 최대 합 저장
    dp[i][j] = dp[i][j] + max(up_left, up)     # 둘 중 비교

print(max(dp[n-1]))