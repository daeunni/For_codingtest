"""
123 더하기 
  - 앞선 [부분수열의 합] 문제와 다른점은 이 문제는 1,2,3 field 내에서 중복 더하기를 허용한다는 것 (이전에는 조합이라 원소간 중복을 허용하지 않았음) 
  - 최대 depth는 1의 개수가 n개일 때이므로, 최대 depth = n으로 잡고 이를 종료조건으로 설정한다. 
  - 이전 풀이보다 이게 조금 더 빠르다! 
"""

def backtracking(cur_sum):
  global count 

  if cur_sum > n :     # 종료조건 
    return 

  for idx in range(len(field)) : 
    cur_sum += field[idx]
    
    if cur_sum == n : 
      count += 1
    
    backtracking(cur_sum)
    cur_sum -= field[idx]

if __name__ == '__main__':
  t = int(input())
  field = [1,2,3]

  for _ in range(t):
    count = 0 
    n = int(input())
    backtracking(0)
    print(count)
