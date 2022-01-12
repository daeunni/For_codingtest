# 숫자카드게임 : 각 행의 min 값 중 max 값을 리턴하기

n, m = map(int, input().split())  # 행 x 열
max_num = 0

for _ in range(n):
    num = list(map(int, input().split()))  # 한 줄씩 리스트로 입력받기

    if max_num < min(num):
        max_num = min(num)

print(max_num)