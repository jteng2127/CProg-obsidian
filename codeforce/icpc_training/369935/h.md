URL: https://codeforces.com/group/dnlUA4rsoS/contest/369935/problem/H

#AC #dp

## Problem

取出最長的子序列a，對所有i符合
a[i-1] < a[i] > a[i+1]
或
a[i-1] > a[i] < a[i+1]

## Solution

```cpp
for(int i = 0; i < n; ++i){
cin >> a[i];
if(i){
  for(int j = 0; j < i; ++j){
	if(a[i] < a[j]) dp[i][0] = max(dp[i][0], dp[j][1]+1);
	if(a[i] > a[j]) dp[i][1] = max(dp[i][1], dp[j][0]+1);
  }
}
ans = max(ans, max(dp[i][0], dp[i][1]));
}
```