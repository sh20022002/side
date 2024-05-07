# recursion fibonacci
def recFib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return recFib(n-1) + recFib(n-2)

# dynamic programming fibonacci with memoization

def memoFib(n, memo=None):
    if memo is None:
        memo = {}
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif n in memo:
        return memo[n]
    else:
        memo[n] = memoFib(n-1, memo) + memoFib(n-2, memo)
        return memo[n]

# dynamic programming fibonacci with tabulation

def tabFib (n):
    tab = [0,1]
    if n <= len(tab):
        return tab[n]
    else:
        i = 2
        for i in range(2,n+1):
            tab.append(tab[i-1] + tab[i-2])
    return tab[n]
def main():
    print(memoFib(10))



if __name__ == "__main__":
    main()
