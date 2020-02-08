#!./env/bin/python

def knapsack(n, C) :
    '''
    0/1 knapsack solution for n < 1000.
    This function builds (n+1) x (C+1) size matrix using bottom-up approach.
    Time Complexity : O(nC). 
    '''
    global memo
    for i in range(1, n+1) :
        for j in range(1, C+1) :
            if j < weights[i] :
                memo[i][j] = memo[i-1][j]
            else :
                memo[i][j] = max(memo[i-1][j], weights[i] + memo[i-1][j-weights[i]])


def backtrace(n, C) :
    '''
    0/1 knapsack solution for n less than 1000.
    This function backtraces to find the elements selected in while
    build the matrix.
    '''
    l = []
    i, j = n, C

    while i >= 0 and j >= 0 :
        if memo[i][j] != memo[i-1][j] :
            l.insert(0, i-1)
            j -= weights[i]
            i -= 1
            continue
        i -= 1

    return l

def choose_greedily(C) :
    '''
    Greedy Approach solution for n >= 1000.
    Time Complexity : O(n). 
    '''
    sol = []
    for i in range(len(weights) - 1, -1, -1)  :
        if C == 0 :
            break
        elif weights[i] > C :
            continue
        else :
            sol.insert(0, i)
            C-=weights[i]
    return sol


if __name__ == "__main__":
    C, n = [int(i) for i in input().split(' ')]
    weights = [int(i)  for i in input().split(' ')]    
    
    if n < 1000 :
        memo = [[0 for i in range(C+1)] for j in range(n+1)]    
        weights.insert(0, 0)

        knapsack(n, C)
        sol = backtrace(n, C)
    else :
        sol = choose_greedily(C)

    print(len(sol))
    [print(i, end = ' ') for i in sol]
    print()