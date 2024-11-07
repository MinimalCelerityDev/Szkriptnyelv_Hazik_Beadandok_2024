city_info = [('Budapest', 1873, 1.752), ('Debrecen', 1361, 0.202),
             ('Szeged', 1183, 0.162), ('Miskolc', 1210, 0.159), 
             ('Pécs', 1009, 0.146), ('Győr', 1009, 0.132)]

print("{:<12} {:<16} {:<12}".format("City", "Year Established", "Population (M)"))
print("-" * 42)
for city in city_info:
    print("{:<12} {:<16} {:<12.3f}".format(city[0], city[1], city[2]))
