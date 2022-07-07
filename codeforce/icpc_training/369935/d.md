URL: https://codeforces.com/group/dnlUA4rsoS/contest/369935/problem/D

#AC #paltree #lca

## Problem

給兩個等長的字串S、T，求每個位置的複製回文字串最長長度k
  S[i−k:i] = T[i:i+k] 都是回文

## Solution

構造 S+"|"+rev(T)，丟回文樹求兩字串對應位置的LCA