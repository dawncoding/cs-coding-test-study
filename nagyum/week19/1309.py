import sys
input=sys.stdin.readline

n = int(input())
if n==1:
    print(3)
else:
    dp=[1 for _ in range(n+1)]
    dp[1]=3
    dp[2]=7
    for i in range(3,n+1):
        dp[i]=(2*dp[i-1]+dp[i-2])%9901
    print(dp[n])