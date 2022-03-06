"""
Distinct
  - 리스트 내 distinct 한 요소의 개수 구하기

1) Counter 모듈 활용 > 시간 복잡도도 괜찮은 듯 !
2) set으로 중복된 값 제거하고 그 길이 출력하기 

"""

from collections import Counter

# sol 1
def solution(A):
  return len(Counter(A))

# sol 2
def solution(A):
  return len(list(set(A)))
