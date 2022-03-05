"""
OddOccurrencesInArray
  - 홀수 개수 리스트에서 혼자 남는 값 찾기

  1) Counter 모듈 활용해 리스트 내 원소의 개수 세기
  2) 2로 나눴을 때 나머지가 1인 value로 key 접근하기 
"""


from collections import Counter

def solution(A):
  dic = Counter(A)
  rev= dict(map(reversed, dic.items()))    # value로 key값 접근하기 
  return [rev[x] for x in dic.values() if x % 2 == 1][0]
