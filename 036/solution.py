print sum(i if str(i) == str(i)[::-1] and
               str(bin(i))[2:][::-1] == bin(i)[2:] else 0
          for i in range(1000000))
