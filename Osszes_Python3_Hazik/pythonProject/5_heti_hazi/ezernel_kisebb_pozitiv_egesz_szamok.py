osszeg = 0

for x in range(1000):
    if x % 3 == 0 or x % 5 == 0:
        osszeg += x

print("A 1000-nél kisebb, 3-mal vagy 5-tel osztható számok összege a következő lesz ==> === ", osszeg)
