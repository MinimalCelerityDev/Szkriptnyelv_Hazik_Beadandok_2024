# 1. Feladat: Rendezés az utolsó oszlop szerint

anyag = [
    (1, 'Albany', 'NY', 162692),
    (121, 'Wyoming', 'NY', 8722),
    (3, 'Allegany', 'NY', 11986),
    (123, 'Yates', 'NY', 5094)

]
rendezett = sorted(anyag, key=lambda x: x[3])

print("Elsőeredményeze ez lesz bizony => ", rendezett)

# 2. Feladat: Rendezés user ID szerint csökkenő sorrendbe

felhasznalok = ['10:User1', '80:User2', '100:User3', '00:User4', '75:User4', '45:User5']

sorted_users = sorted(felhasznalok, key=lambda x: int(x.split(':')[0]), reverse=True)

print( "Második eredményeze ez lesz bizony => ", sorted_users)

# 3. Feladat: Mátrix rendezése a 2. oszlop szerint

matrix = [[2, 6], [1, 3], [5, 4]]

sorted_matrix = sorted(matrix, key=lambda x: x[1])

print("Harmadik eredményeze ez lesz bizony => ", sorted_matrix)
