URL: https://vjudge.net/contest/483013#problem/D

#AC #game

## Problem

標準nim game，但是一堆石頭拿過k顆後，之後就不能再拿k這個數字
例如2拿1變1，那這堆1不能再拿1走，所以就不能繼續操作
一堆石頭數目 <= 60

## Solution

開一個`vector<map<set<K>, SG> >`
把每堆石頭已經拿走哪些數字丟進set一起當作狀態，計算1~60+空set的sg值
直接算會TLE，可能可以優化但我懶得思考直接線下解

我遞迴的時候開一個mex陣列 可是開在全域 所以遞迴下去都會改道直接爛掉 搞笑啊