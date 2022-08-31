# J - ABC Legacy

contest: [[CFICPC/103438/103438|2021 ICPC Southeastern Europe Regional Contest]]
url: https://codeforces.com/gym/103438/problem/J
#Status/READYCORRECT 
Tags: #MEDIUM #括號配對

## Description

給一串長度 `2*n` 的字串，只包含ABC三種字元，問能不能把這個字串切出n組不交疊的子序列，且每個子序列只能是"AB", "AC", "BC"的其中一種。

## Solution

把所有A當右括號
把左邊n - count(A)個B當右括號
其他都左括號
檢查能不能括號匹配就好

思考的切入點：
一開始想說從頭跟尾一個一個處理，但不好思考B怎麼處理
後來去思考怎麼一次把所有字元一次配對完
觀察到他都是兩個字母，可以當成括號配對
觀察到A只會在右邊，當右括號
C一定是左括號
B兩者都可
而配對一定有n個，所以右括號缺的數量一定是用B來補
貪婪想法先取左邊的B最好
最後再驗證括號配對