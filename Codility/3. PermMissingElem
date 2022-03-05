"""
PermMissingElem
  - 리스트 연속된 원소들 중 빠져있는 원소 반환하기 
  - 정상적인 연속된 리스트 합 - 빠져있는 리스트 합 = 빠져있는 원소가 나올 것이라는 아이디어로 접근

  1) 예외 처리를 잘 해야하는 문제 (리스트가 비어있는 경우 등)
  2) 특히, 1~N까지 주어져있고 마지막 원소가 빠진 원소인 경우 ** 

"""

def solution(A):
  if len(A) == 0 :    # 비어있으면 1이 빠져있는거임 
    return 1

  if len(A) + 1 == max(A):   
    return sum([i for i in range(1, max(A)+1)]) - sum(A)

  # 1~N까지 주어져있고 마지막 원소가 빠진 원소인경우..!! 
  else : 
    return max(A) + 1   
