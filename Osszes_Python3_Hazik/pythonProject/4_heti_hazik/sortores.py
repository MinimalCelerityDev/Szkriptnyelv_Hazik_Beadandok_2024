import random as r

egszen_ = 100
sor_hossza_ = 10

def main():
    r.seed(0)
    for i in range(egszen_):
        print(r.randint(0, 9), end="")
        if (i + 1) % sor_hossza_ == 0:
            print()
    print()

if __name__ == "__main__":
    main()
