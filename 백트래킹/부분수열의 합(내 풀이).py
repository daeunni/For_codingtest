"""
부분 수열의 합 
  - 노드를 포함할 때 / 포함하지 않을 때를 고려하는 방법보단 2배 더 비효율 적이지만, 나는 이렇게 풀었다는.. !
  - 로또문제 백트래킹과 비슷한 방식이다. 
"""

# 그냥 별다른 제한 조건 없이 그래프 쭉 뻗은 다음 생각해보자. 
def backtracking(start):
  global cur_sum, count     

  # 종료 조건이 필요하다. > 그냥 depth로 설정하기. 이때 ==로 설정하면 문제가 풀리지 않고, >로 설정해주자. 
  if start > len(field):
    return 

  for idx in range(start, len(field)):
    if cur_sum == int(1e9):
      cur_sum = field[idx]
    else : 
      cur_sum += field[idx]
    if cur_sum == s : 
      count += 1

    backtracking(idx+1)
    cur_sum -= field[idx]
  

if __name__ == "__main__":
  n, s = map(int, input().split())
  field = list(map(int, input().split()))
  cur_sum = int(1e9)
  count = 0
  backtracking(0)
  print(count)
