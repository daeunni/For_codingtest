"""
오븐 시계
"""

h, m = map(int, input().split())     # 현재 시각
need = int(input())                  # 요리에 필요한 시각

final_h = h + ((m + need) // 60)     # 몫 더해주기
final_m = (m + need) % 60

# 24시 이상의 시각은 변경해주기
if final_h >= 24:
  final_h = final_h % 24

print(final_h, final_m)