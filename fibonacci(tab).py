def fib_tab(length):
    dp = [0] * (length+1)

    dp[1] = 1

    for i in range(2, length+1):
        dp[i] = dp[i-1] + dp[i-2]
    
    return dp[length]

if __name__ == '__main__':
    print(fib_tab(50))