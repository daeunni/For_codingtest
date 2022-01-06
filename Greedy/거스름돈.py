
# coin : 500, 100, 50, 10 won > minimum count

N = 1260
wallet = [500, 100, 50, 10]

def change_money(N, wallet):
    count = 0
    for coin in wallet:
        count += N // coin
        N %= coin

    print(count)

change_money(N, wallet)