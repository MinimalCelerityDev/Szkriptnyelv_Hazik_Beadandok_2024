def saktabla(a_kiralyno):

    print("+" + "-" * 17 + "+")

    for row in range(8):
        line = "|"
        for col in range(8):

            if a_kiralyno[col] == row:
                line += " Q"
            else:
                line += " ."
        line += " |"

        print(line)

    print("+" + "-" * 17 + "+")


# Példa input
queens = [0, 4, 7, 5, 2, 6, 1, 3]
saktabla(queens)
