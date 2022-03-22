"""
기타줄 
  - 경우의 수 3개를 고려해 각각을 구현하는 문제 
  - 1) 6개 + 남는 것 낱개 구매 
    2) 모두 낱개 구매 
    3) 넘더라도 6개짜리로 구매 
"""

n, m = map(int, input().split())
min_price = 999999999999999
min_six = 9999999
min_one = 9999999

# <경우> 1) 6개 + 남는 것 낱개 / 2) 모두 낱개 / 3) 넘더라도 6개짜리로 구매 
def exam(six, one, n):
  a = six * (n//6) + one * (n%6)
  b = one * n
  c = six * (n//6 + 1)
  return min(a, b, c)

for _ in range(m):      # m개의 브랜드
  six, one = map(int, input().split())
  min_price = min(exam(six, one, n), min_price)

  # 다른 케이스끼리 조합하는 경우 고려 : 아마 이는 가장 작은 six, one 값에서 발생할 것이라고 생각 
  min_six = min(min_six, six)
  min_one = min(min_one, one)

print(min(exam(min_six, min_one, n), min_price))
