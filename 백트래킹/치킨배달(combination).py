"""
치킨 배달 
  - 그냥 combination으로 먼저 풀어보자 
"""
from itertools import combinations

# 해당 치킨집 조합과 1들의 거리를 리턴하는 함수 
def distance(one_list, two_ele) : 
  dis = 0 
  for one_ele in one_list : 
    how_min = 99999 
    for t in two_ele : 
      # 둘 중 min 값만 저장 
      how_min = min(abs(one_ele[0] - t[0]) + abs(one_ele[1] - t[1]), how_min)
    dis += how_min
  return dis


if __name__ == '__main__':
  N, M = map(int, input().split())
  m = []     # map 
  result = 999999    # 도시의 치킨거리 최솟값 

  for _ in range(N):
    m.append(list(map(int, input().split())))

  # 1과 2 위치 적재 
  ones = [] ; twos = []
  for i in range(N):
    for j in range(N):
      if m[i][j] == 1 : 
        ones.append((i+1, j+1))   # 튜플로 적재 
      elif m[i][j] == 2 : 
        twos.append((i+1, j+1))

  chi = list(combinations(twos, M))       # 치킨집 M개 고르는 경우의 수 

  # 치킨집 조합별 반복문 
  for two_ele in chi : 
    result = min(result, distance(ones, two_ele))

  print(result)
