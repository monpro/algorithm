

print("executed before main")
def solution_dp(length):
    if length < 2:
        return 0
    elif length == 2:
        return 1
    elif length == 3:
        return 2
    dp = [0 for _ in range(length + 1)]
    dp[0] = 0
    dp[1] = 1
    dp[2] = 2
    dp[3] = 3

    for i in range(4,length + 1):
        temp = 0
        for j in range(i//2 + 1):
            temp = max(temp, dp[j] * dp[i - j])
        print(temp)
        dp[i] = temp
    print(dp)
    return dp[length]


if __name__ == "__main__":
    print(solution_dp(8))
