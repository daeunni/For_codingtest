"""
PermCheck
  - 1~N까지 모두 나왔는지 확인 
  - visited list 활용하기 
  - 모두 등장했는지 확인할 때는 check_num 활용하기 (더해서 확인 X)
"""

def solution(A):
  visited = [0 for _ in range(len(A))]
  check_num = 0 
  
  # 예외1) 리스트가 빈 리스트일 때 / 예외2) 원소가 len보다 클 때 
  if len(A) == 0 or max(A) > len(A):
    return 0

  for num in A : 
    if visited[num-1] == 0 : 
      visited[num-1] = 1
      check_num += 1

  # 순열 가능 
  if check_num == len(A):
    return 1

  else:
    return 0
