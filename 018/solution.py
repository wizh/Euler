pyra = [[int(i) for i in l.strip('\n').split(' ')]
                for l in open('pyra.txt').readlines()]

for i in range(2, len(pyra) + 1):
    for j in range(len(pyra[-i])):
        pyra[-i][j] = pyra[-i][j] +  max(pyra[-i+1][j], pyra[-i+1][j+1])

print pyra[0][0]
