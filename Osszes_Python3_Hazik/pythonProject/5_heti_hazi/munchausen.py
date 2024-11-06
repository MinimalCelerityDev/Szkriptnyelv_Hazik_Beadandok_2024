

def ez_munchausen(n):
    #ebben volt kis net segítségem, be vallom őszintén
    return n == sum(int(digit) ** int(digit) if digit != '0' else 0 for digit in str(n))

print("10 000.nél kisebb munchausen szamok itt vannak ===>")
for i in range(10000):
    if ez_munchausen(i):
        print(i)

print("\n440.nél kisebb munchausen szamok itt vannak ===>")
for i in range(440000000):
    if ez_munchausen(i):
        print(i)
