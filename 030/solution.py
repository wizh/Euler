print sum(n if sum([int(i)**5 for i in str(n)]) == n else 0
                              for n in range(2, 1000000))
