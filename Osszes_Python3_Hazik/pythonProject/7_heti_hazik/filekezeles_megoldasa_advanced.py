def main():
    f = open("string1_megoldás.py", "r")
    r = open("string1_megoldás_advanced.py", "w")
    for line in f:
        s = line
        if "#" not in s:
            r.write(line)
    r.close()
    f.close()

if __name__ == "__main__":
    main()