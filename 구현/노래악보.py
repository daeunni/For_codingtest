"""
노래악보 
  - 문제를 이해하는데 오래걸렸던 유형.. 
  - 리스트로 해결
"""

n, q = map(int, input().split())
time_list = []
ques_list = []
main = []

# input 입력 
for _ in range(n):
  time_list.append(int(input()))
for _ in range(q):
  ques_list.append(int(input()))

# 구현 
for i, j in enumerate(time_list):
  main += [i+1 for _ in range(j)]

# 출력 
for idx in ques_list : 
  print(main[idx])
