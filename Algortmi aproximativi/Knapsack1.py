def maximum_sum_dp(S, K):
    n = len(S)
    dp = [[-1] * (K + 1) for _ in range(n + 1)]
    
    # Initializare
    dp[0][0] = 0
    
    # Calculare
    for i in range(1, n + 1):
        for j in range(K + 1):
            if dp[i - 1][j] >= 0:
                dp[i][j] = dp[i - 1][j]
            elif j >= S[i - 1] and dp[i - 1][j - S[i - 1]] >= 0:
                dp[i][j] = dp[i - 1][j - S[i - 1]] + S[i - 1]
    
    # Găsirea sumei maximale
    max_sum = -1
    for j in range(K + 1):
        if dp[n][j] >= 0:
            max_sum = max(max_sum, dp[n][j])
    
    return max_sum

# Exemplu de utilizare:
S = [10, 2, 3, 4, 9]
K = 8
print("Suma maxima sub K:", maximum_sum_dp(S, K))
