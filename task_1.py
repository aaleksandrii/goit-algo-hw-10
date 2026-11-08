import timeit

COINS = [50, 25, 10, 5, 2, 1]


def find_coins_greedy(value: int) -> dict[int, int]:
    result = {}
    for coin in COINS:
        if value >= coin:
            count = value // coin
            result[coin] = count
            value -= coin * count
    return result


def find_min_coins(value: int) -> dict[int, int]:
    dp = [float("inf")] * (value + 1)
    dp[0] = 0

    coin_used = [0] * (value + 1)

    for i in range(1, value + 1):
        for coin in COINS:
            if coin <= i and dp[i - coin] + 1 < dp[i]:
                dp[i] = dp[i - coin] + 1
                coin_used[i] = coin

    result = {}
    while value > 0:
        coin = coin_used[value]
        result[coin] = result.get(coin, 0) + 1
        value -= coin

    return dict(sorted(result.items()))


if __name__ == "__main__":
    print(f"\n Value: {113}")
    print(f"> greedy: {find_coins_greedy(113)}")
    print(f"> dynamic programing: {find_min_coins(113)}")

    print("\n---------")
    print("timeit, number 1000")
    for value in [113, 1_000, 10_000]:
        t_greedy = timeit.timeit(lambda: find_coins_greedy(value), number=1000)
        t_dp = timeit.timeit(lambda: find_min_coins(value), number=1000)
        print(f"\n Value {value}:")
        print(f"> greedy: {t_greedy:.4f} s")
        print(f"> dynamic programing: {t_dp:.4f} s")