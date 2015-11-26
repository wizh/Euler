ts, ps, hs, count = [], [], [], 0
while(1):
    ts += [int(count * (1 * count + 1) / 2)]
    ps += [int(count * (3 * count - 1) / 2)]
    hs += [int(count * (2 * count - 1))]
    count += 1

    if len(ts) > 286 and ts[count - 1] in ps and ts[count - 1] in hs:
        break

print ts[-1]
