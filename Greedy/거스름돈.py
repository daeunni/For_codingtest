
"""
최소 개수의 동전으로 N원을 만들기 
"""

N = 1260
wallet = [500, 100, 50, 10]

def change_money(N, wallet):
    count = 0
    for coin in wallet:
        count += N // coin     # 몫만큼 count에 더하고 
        N %= coin          # 나머지를 남기기 

    print(count)

change_money(N, wallet)
