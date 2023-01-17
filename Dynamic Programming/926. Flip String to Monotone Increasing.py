"""
Leetcode today's problem 
  - 00111 의 monotone 형태로 array를 만들려고 하고, 특정 인덱스 문자의 flip(0>1, 1>0)이 허용됨. 
  - 최소한의 flip 개수를 구하기 
"""

# DP 문제 : 문제를 sub 문제로 분류하자 
def minFlipsMonoIncr(self, s: str) -> int:
    one = 0                          # sub array 내의 1의 개수 
    flip = 0                         # flip 횟수 
    for sub in s : 
        if sub == '0':               # 마지막 원소가 1인 sub array는 flip을 할 필요가 없다. 
            flip = min(one, flip+1)  # 0을 flip할 때(지금까지의 flip 개수에서 1을 추가하겠다는 뜻)와 안할 때(앞에 1을 모두 뒤집어야함) 둘 중 뭐가 이득인지 min으로 판단한다. 
        else : 
            one += 1
    return flip 
  
 
