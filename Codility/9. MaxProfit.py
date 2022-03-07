"""
MaxProfit
  - 리스트 내에서 주식 가격의 가장 큰 이익을 구하는 문제
  - 인덱스의 순서는 유지하면서, 효율적으로 이익이 큰 경우를 탐색하는게 어려운 문제

1) 무조건 << []-작은값 >> 을 빼야 최대 이익을 얻을 수 있는 것은 자명하다
2) 순서대로 리스트 원소를 순회하면서 1) min값   2) profit값 을 업데이트하는 방식을 이용한다 ! 
"""

A = [23171, 21011, 21123, 21366, 21013, 21367]

def solution(A):

  # 예외 1) element 수가 적어 이익을 계산할 수 없을 때 
  if len(A) < 2:
    return 0

  # 최솟값은 우선 첫번째 원소로 잡는다
  min = A[0]
  profit = 0

  for price in A : 
    present = price - min     # 현재의 이익 

    # 현재 이익이 더 크면 업데이트 
    if profit < present : 
      profit = present

    # 최솟값 더 작으면 업데이트 
    if min > price : 
      min = price
    
    # >> 이러한 방식으로 하면 인덱스도 유지된다. 

  return profit

solution(A)
