# J - Java Certification

contest: [[CFICPC/100069/100069|2009-2010 ACM-ICPC Northeastern European Regional Contest (NEERC 09) (Deprecated, without interactive problem C)]]
url: https://codeforces.com/gym/100069/problem/J
Status: #READYTOTRY
Tags: #EASY #暴搜 

## Description

總共n題，全部的題目都被分到m種類別，你知道所有類別的正確率四捨五入的結果，也知道總共對了k題，要你猜測每種類別的題數 $n_i$ 分別是多少與分別錯幾題。可能有很多種結果，要取 $max(\{n_i\}) - min(\{n_i\})$ 最小的結果，如果有很多種最小，任一最小皆可

n≤100
m≤10

## Solution

用n找出所有正確率可能的題數是多少 $O(n^2)$ 或 $O(nm)$
再dfs爆搜所有類別可能的題數，找出正確答案，8e10=1,073,741,824，所以每個類別可能的題數都落在8種左右以下就可以過