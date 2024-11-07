def main():
    f = open("string1.py", "r")
    r = open("string1_megoldás.py", "w")
    for line in f:
        if line[0] != "#":
            r.write(line)
    r.close()
    f.close()

if __name__ == "__main__":
    main()