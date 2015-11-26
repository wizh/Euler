ts = [int(0.5 * i * (i + 1)) for i in range(20)]
print sum(sum((ord(c) - 64) for c in w) in ts
                            for w in open('words.txt').read().split(' '))
