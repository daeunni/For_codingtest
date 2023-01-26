"""
로또 
  - 조합(combination)에 backtracking을 적용하는 법 
  - Data field의 원소를 하나씩 훑으면서 pop 해준다. 
  - 먼저 그래프 들을 그리고 각 노드를 뻗는 공통된 "단위"가 뭔지를 파악해, 그걸 for 문의 단위로 설정한다. 
"""

# com에서 6개의 조합 선택하기 
def com_backtracking(start):
  if len(cur) == 6 : 
    print(cur[0], cur[1], cur[2], cur[3], cur[4], cur[5])     # return 
    return 

  for idx in range(start, len(field)):    # 1씩 차이나도록 세팅 
    if len(cur) < 6 : 
      cur.append(field[idx])
      com_backtracking(idx+1)    # 그 다음 idx 
      cur.pop()

if __name__ == '__main__':

  # Input 
  all_dt = []
  while True : 
    s = list(map(int, input().split()))
    if s[0] == 0 :            # Input ending condition  
      break
    all_dt.append(s[1:])      # data field 

  # Conduct code 
  for field in all_dt : 
    cur = []
    com_backtracking(0)
    print(' ')
