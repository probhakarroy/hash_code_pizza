#!./env/bin/python
import numpy as np

def knapsack(n, C) :
    global memo
    
    if memo[n][C] != 0 :
        return memo[n][C]
    elif n < 0  or C <= 0 :
        result = 0
    elif weights[n] > C :
        result = knapsack(n-1, C)
    else :
        result = max(knapsack(n-1, C), weights[n] + knapsack(n-1, C-weights[n]))
    
    memo[n][C] = result
    memo.flush()
    return result

def backtrace(n, C) :
    l = []
    i, j = n, C

    while i >= 0 and j >= 0 :
        if memo[i][j] != memo[i-1][j] :
            l.append(i-1)
            j -= weights[i]
            i -= 1
            continue
        i -= 1
    
    l.reverse()
    return l

if __name__ == "__main__":
    C, n = [int(i) for i in input().split(' ')]
    weights = [int(i)  for i in input().split(' ')]    
    
    memo = np.memmap('temp', mode = 'w+', shape = (n+1, C+1))
    weights.insert(0, 0)

    knapsack(n, C)
    sol = backtrace(n, C)
    print(len(sol))
    [print(i, end = ' ') for i in sol]
    print()