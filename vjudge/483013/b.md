URL: https://vjudge.net/contest/483013#problem/B

#AC #game

## Problem

標準賽局，n顆石頭，每次只能拿取連續的1~k顆石頭

## Solution

如果 n >= 3, k >= 2 就一定可以把遊戲拆成兩個一樣的獨立賽局
其賽局和的特徵值就一定為0 先手勝

整理一下得到
n = 0 或 k = 1, n is even -> 後手勝
其他先手勝