def main():

    with open("table.txt", "r") as f:

        l = [i.rstrip("\n") for i in f.readlines()]

        sorErtekek = []

        for sor in l:

            sorErtekek.append(sor.split())

        max_values = [max(map(int, i)) for i in sorErtekek]

        min_values = [min(map(int, j)) for j in sorErtekek]

        kulonbsegek = []

        for k in range(len(max_values)):

            kul = 0

            kul = max_values[k] - min_values[k]

            kulonbsegek.append(kul)

        print("ell " + str(sum(kulonbsegek)))


if __name__ == "__main__":
    main()