"""
치킨 배달
"""
def distance(i, j, two):
  """
  - Input : 1의 좌표 (i, j) + map 내 모든 치킨집들의 좌표 모음 
  - Output : distance list 
  """
  dis = []
  for chi_zip in two : 
    x = chi_zip.split(',')[0]
    y = chi_zip.split(',')[1]
    dis.append(abs(i-int(x)) + abs(j-int(y)))
  return dis

def find_chicken(map):
  """
  - Input : map list 
  - Output : map 안의 모든 치킨집의 좌표 
  """
  two = []
  for i in range(N):
    for j in range(N):
      if m[i][j] == 2 : 
        two.append(str(i) + ',' + str(j))
  return two 


def dfs(i, j, two):
  global all_cd         # 모든 집, 치킨집 조합에 대한 치킨거리 계산 

  if i < 0 or j < 0 or i > N or j > N : 
    return all_cd

  # 일반 집이면 M개에 대해 치킨거리 계산 
  if m[i-1][j-1] == 1 : 
    all_cd.append(distance(i, j, two))
    print(all_cd)
  
  dfs(i+1, j, two)
  dfs(i, j+1, two)
  return all_cd 

if __name__=='__main__':
  N, M = map(int, input().split())
  m = []
  for _ in range(N):
    m.append(list(map(int, input().split())))
  result = 999999999    # 도시의 치킨거리 최솟값 

  two = find_chicken(m)  # map 내 모든 치킨집 좌표 모음 
  all_cd = []
  all_cd = dfs(1, 1, two)    # 일부러 (1, 1)에서 시작 
  print(all_cd)

  # 최소 치킨거리 값 업데이트 
  all_sum = 0 
  for i in range(len(two)) :
    for j in range(len(all_cd)) : 
      all_sum += all_cd[j][i]
    result = min(result, all_sum)
  print(result)
