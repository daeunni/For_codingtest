# 우선 재귀함수로 피보나치 구현
def fibo(x):
    if x == 1 or x == 2:
        return 1
    else:
        return fibo(x - 1) + fibo(x - 2)  # x항 = x-1항 + x-2항


"""
하향식 DP를 이용해 한번 계산한 결과 <메모이제이션(Memoization)>
"""

d = [0] * 100  # 저장공간 만들기


def fibo_dp(x):
    if x == 1 or x == 2:
        return 1

    # 만약 이전에 계산한 결과가 존재한다면
    if d[x] != 0:
        return d[x]

    # 존재하지 않는다면 새로 재귀함수로 계산해 리턴
    d[x] = fibo_dp(x - 1) + fibo_dp(x - 2)
    return d[x]