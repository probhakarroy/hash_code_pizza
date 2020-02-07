#!./env/bin/python
import numpy as np

def knapsack(n, C) :
    global memo
    for i in range(n+1) :
        print('Matrix Creation Progress : {}/{}'.format(i, n), end='\r')
        for j in range(C+1) :
            if i == 0 or j == 0 :
                memo[i][j] = 0
            elif j < weights[i] :
                memo[i][j] = memo[i-1][j]
            else :
                memo[i][j] = max(memo[i-1][j], weights[i] + memo[i-1][j-weights[i]])


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
    print()
    sol = backtrace(n, C)
    print(len(sol))
    [print(i, end = ' ') for i in sol]
    print()