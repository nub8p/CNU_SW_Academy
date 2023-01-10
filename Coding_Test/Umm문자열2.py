import sys
input = sys.stdin.readline

for _ in range(int(input())):
    s, m = map(int, input().split())
    inputs = input()

    dp = [0] * s # using DP
    for i in range(s):
        if inputs[i] == 'U':
            dp[i] = 1
        if i == 0: continue
        elif inputs[i] == 'm' and inputs[i - 1] == 'U':
            dp[i] = dp[i - 1] + 1
        elif inputs[i] == 'm' and inputs[i - 1] == 'm':
            if dp[i - 1] == 0: continue
            dp[i] += dp[i - 1] + 1

    result = 0
    for __ in range(m):
        a, b = map(int, input().split())
        len_Umm = dp[b - 1] - dp[a - 1]
        if dp[a - 1] == 1 and b - a == len_Umm and len_Umm >= 2:
            result += 1

    print(result)

