URL: https://vjudge.net/contest/483013#problem/C

#AC #game #dp

## Problem

n顆石頭，問你有幾種分法可以先手必勝 (順序不同即為不同分法，例如 {1,1,2} 跟 {1,2,1} 是兩種)

## Solution

二維dp配sg概念
`dp[i][j]` 代表 i 顆石頭組出sg值為 j 有幾種方法
轉移式：
`for i in [1:100], for j in [0:i-1], for k in [0:j]`
`dp[i][(i-j)^k] += dp[j][k]`
再把特徵值不為0的數量都加起來