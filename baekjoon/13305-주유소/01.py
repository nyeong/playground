def solve(roads, oil_prices):
    most_cheap = oil_prices[0] + 1
    total_price = 0
    for road, oil_price in zip(roads, oil_prices):
        most_cheap = min(oil_price, most_cheap)
        total_price += road * most_cheap
    return total_price

if __name__ == '__main__':
    from sys import stdin
    n = int(stdin.readline())
    roads = map(int, stdin.readline().split())
    oil_prices = list(map(int, stdin.readline().split()))
    print(solve(roads, oil_prices))
