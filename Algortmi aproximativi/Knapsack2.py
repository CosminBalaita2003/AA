def approximate_maximum_sum(S):
    S.sort(reverse=True)
    current_sum = 0
    total_sum = 0
    for num in S:
        total_sum += num
    for num in S:
        if current_sum + num <= total_sum / 2:
            current_sum += num
        else:
            break
    return current_sum

# Exemplu de utilizare:
S = [1, 2, 3, 4, 5]
print("Suma aproximativă:", approximate_maximum_sum(S))
