#!./env/bin/python

def knapsack(n, C) :
    global memo
    for i in range(1, n+1) :
        for j in range(1, C+1) :
            if j < weights[i] :
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
    
    memo = [[0 for i in range(C+1)] for j in range(n+1)]
    
    weights.insert(0, 0)

    knapsack(n, C)
    sol = backtrace(n, C)
    
    print(len(sol))
    [print(i, end = ' ') for i in sol]
    print()