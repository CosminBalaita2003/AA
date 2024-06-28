def determine_intersection():
    n = int(input().strip())
    
    semiplanes = []
    for _ in range(n):
        ai, bi, ci = map(int, input().strip().split())
        semiplanes.append((ai, bi, ci))
    

    min_x, max_x = -float('inf'), float('inf')
    min_y, max_y = -float('inf'), float('inf')
    
    for (ai, bi, ci) in semiplanes:
        if ai != 0:  # semiplan vertical
            if ai > 0:
                max_x = min(max_x, -ci / ai)
            else:
                min_x = max(min_x, -ci / ai)
        else:  # semiplan orizontal
            if bi > 0:
                max_y = min(max_y, -ci / bi)
            else:
                min_y = max(min_y, -ci / bi)
    
    if min_x > max_x or min_y > max_y:
        print("VOID")
    elif min_x == -float('inf') or max_x == float('inf') or min_y == -float('inf') or max_y == float('inf'):
        print("UNBOUNDED")
    else:
        print("BOUNDED")

determine_intersection()
