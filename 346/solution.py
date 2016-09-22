def to_base(n, base):
    digits = []
    while n > 0:
        digits.insert(0, n % base)
        n = n // base
    return digits

def repunit(digits):
    for d in digits:
        if d != 1:
            return False
    return True

def main(n):
    ret = 1
    for i in range(2, n):
        reps = 0
        for j in range(2, i):
            reps += repunit(to_base(i, j))
            if reps > 1:
                ret += i
                break
    return ret

main(10**12)