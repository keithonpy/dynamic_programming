# classic recursive approach
def fib(i):
    if i <= 2:
        return 1
    return fib(i - 1) + fib(i -2)

# Let's break down the problem
def countdown(i):
    if i <= 1:
        return
    return countdown(i-1)

def countdown2(i):
    if i <= 1:
        return
    return countdown2(i-2)


# dp memoization
dp = {}
def fib_memo(i):
    if i <= 2:
        return 1
    if i in dp:
        return dp[i]
    
    dp[i] = fib_memo(i-1) + fib_memo(i-2)

    return dp[i]


if __name__ == '__main__':
    print(fib_memo(50))