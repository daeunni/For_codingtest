"""
PermMissingElem
  - P를 중심으로 양쪽으로 리스트를 나눈 후, 합에 대해 연산해 최솟값 반환하기 
  
  1) 시간 복잡도를 줄여야하는 문제 (for문으로 돌아가면서 sum을 하면 그만큼 복잡도가 늘어난다)
  2) 최대한 for문 내에서 sum을 하지 않는 방식으로 작동하도록,,,!!!

"""

def solution(A):
  sum1 = 0
  sum2 = sum(A)
  result = 1e6

  # 원소가 하나인 상황? > P를 정할 수 없음 
  if len(A) == 1 : 
    return 0 

  for p in range(1, len(A)):

    # 더하는 과정의 복잡도를 줄이기 위함이다!!! (하나씩 빼서 sum으로 생각)
    sum1 += A[p-1]      # 인덱스니까 p-1로 해줘야함 !
    sum2 -= A[p-1]
    result = min(result, abs(sum1-sum2))   

  return result

solution([1])
