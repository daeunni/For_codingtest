# 1이 될때까지 연산하기

n, k = map(int, input().split())
min_count = 0      # 1을 만드는 최소 횟수 반환
ans = n        # 이게 1이될 때까지 연산하기

while ans != 1:        # 참일때까지 연산

  # k로 나눠지면
  if ans % k == 0 :
    ans /= k      # 몫을 저장
    min_count += 1

  else:
    ans -= 1
    min_count += 1

print(min_count)