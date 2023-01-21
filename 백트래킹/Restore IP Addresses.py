"""
93. Restore IP Addresses
  - 아이디어 접근까지는 정확히 맞았지만, 구현력이 떨어져서 실패한 문제다 ㅠ 
  - 전형적인 백트래킹 문제 
  - 문자열이 주어지면 1)1~255  2)0으로 시작하지 않게 4개의 부분으로 점으로 나눠 반환하는 문제!
"""

def backtracking(start):

  # node final 
  if len(s) == start and len(cur_node) == 4 : 
    valid_ip.append('.'.join(cur_node))     # list append 
    return 
  
  # 후보 노드 고려 
  for window in range(1, 4):
    cur = s[start:start+window]
    
    # 조건에 안맞으면 넘어가기  
    if len(cur) > 1 and (int(cur) > 255 or cur[0] == '0') : 
      continue 

    # 조건에 맞으면 append 
    if len(cur_node) < 4:          # 이 조건이 아니라 else면 오류가 난다. 
      cur_node.append(cur)
      backtracking(start+window)   # start node 재설정 후 재귀함수 
      cur_node.pop() 

s = '25525511135'
valid_ip = []
cur_node = []
backtracking(0)
