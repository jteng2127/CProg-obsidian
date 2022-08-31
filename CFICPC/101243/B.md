# B - Hanoi tower

contest: [[CFICPC/101243/101243|2016-2017 ACM-ICPC, NEERC, Central Subregional Contest]]
url: https://codeforces.com/gym/101243/problem/B
#Status/READYTOTRY 
Tags: #

## Description

## Solution

想法：
有點公式解
利用玩河內塔最佳步驟的特性（遞迴）
先移n/3×2-1個到B
移1個A到C
並再B整個移上C之間的某個狀態會是平均的
6 9 12的case模擬出來應該就知道了
