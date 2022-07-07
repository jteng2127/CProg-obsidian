URL: https://vjudge.net/contest/483013#problem/H

#AC #game

## Problem

標準賽局，n堆石頭，兩種操作
1. 挑一堆拿掉一顆
2. 挑一堆偶數個 `2 * x` 的石頭，移除並放入 k 個數量為 `x` 的石頭堆

## Solution

對於操作二跟特徵值的特性
k是奇數相當於把那堆減半
k是偶數相當於移除那一堆

觀察sg值的表跟特性找規律
遞迴求sg值