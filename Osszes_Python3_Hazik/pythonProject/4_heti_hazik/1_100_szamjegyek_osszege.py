ez_az_osszeg = 0

for s in range(1, 101):

    for i in str(s):
        ez_az_osszeg += int(i)

print("Az 1-től 100-ig számjegyek összege ez lesz bizony => :", ez_az_osszeg)
