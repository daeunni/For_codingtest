"""
Dominator
  - 리스트 내에서 절반 이상(+과반수) 발생하는 원소의 인덱스 리턴 
  - Counter의 most_common(1) 함수를 이용한다!
"""

from collections import Counter

def solution(A):

  # 예외 1) 리스트 비어있을 때 
  if len(A) == 0 :
    return -1 

  domi = Counter(A).most_common(1)[0]    # Counter 내장 함수인 most_common 사용하기 !!

  if domi[1] > len(A)//2:
    return A.index(domi[0])
  else:
    return -1
