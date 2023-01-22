"""
Palindrome Partitioning
  - 앞뒤로 읽었을 때 똑같은 sub 문자열로 주어진 문자열 나누기
  - IP 문제와 비슷한 백트래킹 접근으로 풀었다. 하지만 속도 측면에서 매우 비효율 적인듯... 
"""

def backtracking(start):
  if len(s) < 2 : 
    final.append(list(s))
    return 

  if start == len(s) :
    final.append(list(cur_list))
    return 

  for size in range(len(s)+1):
    cur_s = s[start : start+size]

    if len(cur_s) > 0 and (cur_s == cur_s[::-1]) :
      cur_list.append(cur_s)
      backtracking(start + size)
      cur_list.pop()

if __name__=='__main__':
  s = "abb"
  cur_list = []
  final = []
  backtracking(0)
  print(final)
