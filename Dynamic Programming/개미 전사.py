"""
개미 전사
  - 연속해서 방문 X. 식량의 최댓값 구하기
  - 배낭 문제와 비슷! (왼쪽부터 차례로 i번째 식량창고를 털지 안털지를 max 값으로 결정한다)
    > 왼쪽부터 차례로 터는게 포인트 !! (bottom-up 방식으로 진행)
"""

N = int(input())   # 식량 창고의 개수
array = list(map(int, input().split()))      # 식량 창고 정보를 list로 입력받기

# i번째 창고를 털었을 때 식량 현황을 DP 테이블에 저장
d = [0] * 100        # 최대 식량창고 개수 100개

d[0] = array[0]
d[1] = max(array[0], array[1])

# 왼쪽부터 차례로 식량창고 털기
for i in range(2, N):
  d[i] = max(d[i-1], d[i-2] + array[i])       # d[i-1] : 현재 식량창고를 털지 않는다 / d[i-2] + array[i] : 현재 식량창고를 턴다

print(d[N-1])      # 인덱스니까 N-1