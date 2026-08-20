# 0/1 Knapsack using Dynamic Programming

weights = [2, 3, 4, 5]
values = [3, 4, 5, 6]
capacity = 5
n = len(weights)


# -------- Bottom-Up --------
def bottom_up():
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(1, capacity + 1):
            if weights[i - 1] <= w:
                dp[i][w] = max(
                    values[i - 1] + dp[i - 1][w - weights[i - 1]],
                    dp[i - 1][w]
                )
            else:
                dp[i][w] = dp[i - 1][w]

    return dp[n][capacity]


# -------- Top-Down --------
def top_down(i, w, dp):
    if i == 0 or w == 0:
        return 0

    if dp[i][w] != -1:
        return dp[i][w]

    if weights[i - 1] <= w:
        dp[i][w] = max(
            values[i - 1] + top_down(i - 1, w - weights[i - 1], dp),
            top_down(i - 1, w, dp)
        )
    else:
        dp[i][w] = top_down(i - 1, w, dp)

    return dp[i][w]


# Results
print("Bottom-Up:", bottom_up())

dp = [[-1] * (capacity + 1) for _ in range(n + 1)]
print("Top-Down:", top_down(n, capacity, dp))