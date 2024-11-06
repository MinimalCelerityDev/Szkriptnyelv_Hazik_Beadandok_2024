def negyzetek_osszege_(n):
    sum_squares = 0
    for i in range(1, n + 1):
        sum_squares += i * i
    return sum_squares

def osszegek_negyzete_(n):
    total_sum = 0
    for i in range(1, n + 1):
        total_sum += i
    return total_sum * total_sum

n = 100

sum_squares = negyzetek_osszege_(n)

square_sum = osszegek_negyzete_(n)

kulonbseg = square_sum - sum_squares

print("Az első", n, "természetes szám összegének a négyzete:", square_sum)

print("Az első", n, "természetes szám négyzetösszege:", sum_squares)

print("A különbség:", kulonbseg)
