ps = [0] * 1000
for i in range(1000):
    for j in range(1000):
        d = (i**2 + j**2)**0.5
        p = i + j + d
        if p.is_integer() and p < 999:
            ps[int(p)] += 1

print ps.index(max(ps))
