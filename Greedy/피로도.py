## 하루 1시간 일하기 : 피로도는 A만큼, 일은 B만큼 처리
## 하루 1시간 쉬기 : 피로도 C만큼 줄어듦 

## 피로도가 M을 넘지 않도록 일하기 > 하루 24시간 동안 최대 얼마나 일할 수 있을까? 

a, b, c, M = map(int, input().split())
sleep = 0  # 피로도
work = 0  # 일 양  > 최대로 만들어야함
time = 0  # 하루 시간

# 24시간 동안 반복 
while time < 24:
    if a > M:
        break

        # 피로도 계산 식
    if sleep + a <= M:
        sleep += a
        work += b
        time += 1

    else:
        sleep -= c
        time += 1

    if sleep < 0: sleep = 0

print(work)