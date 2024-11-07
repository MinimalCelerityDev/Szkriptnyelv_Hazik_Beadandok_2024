def main():
    page = input("Add meg a nyomtatandó oldalakat: ")
    oldalak = []
    rangePage = []
    kesz = []
    if "," not in page:
            if "-" in page:
                rangePage = page.split("-")
                for i in range(int(rangePage[0]), int(rangePage[1]) + 1):
                    kesz.append(str(i))
            else:
                kesz.append(page)
    else:
        oldalak = page.split(",")
    for o in oldalak:
        if "-" in o:
            rangePage = o.split("-")
            for i in range(int(rangePage[0]), int(rangePage[1]) + 1):
                kesz.append(str(i))
        else:
            kesz.append(o)

    res = ",".join(kesz)
    print(res)


if __name__ == "__main__":
    main()