URL: https://codeforces.com/gym/103185/problem/B

#AC #暴搜 #調和級數

## Problem

給你一串高度，一座山的定義是區間內先上坡再下坡，問你是否存在k可以把那串高度拆成k個k個一組，並且每個區間都是一座山，最後如果剩不到k個就直接算
(自己看題目比較好懂)

## Solution

[官解](https://github.com/Diego1149/ICPC-Latam-2020/blob/main/B/Source.cpp)
有限自動狀態機，篩掉k，sieve估時間複雜度

[評論解](https://codeforces.com/blog/entry/92792?#comment-826855)
窮舉k，二分搜處理未知數，再O(1)判斷是不是山、調和級數算時間複雜度 $O(n\log^2{n})$
下面評論說可以用稀疏表壓到$O(n\log{n})$

[CSDN解](https://blog.csdn.net/m0_53603552/article/details/120803025)
前處理左右下坡的最長長度(-1不好處理QQ)、窮舉k、O(1)判是不是山
$O(n\log{n})$
我就是用這ㄍ