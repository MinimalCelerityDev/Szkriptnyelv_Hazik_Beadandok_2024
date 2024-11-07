string_1 = "{[]{()}}"
string_2 = "((5+3)*2+1)"
string_3 = "{[(3+1)+2]+}"
string_4 = "(3+{1-1)}"
string_5 = "(({[(((1)-2)+3)-3]/3}-3)"

def main(s):
    sum_1 = 0
    sum_2 = 0
    sum_3 = 0
    sum_4 = 0
    sum_5 = 0
    sum_6 = 0
    sum_save = 0
    for i in range(len(s)):
        if s[i] == "(":
            sum_1 += 1
        elif s[i] == "[":
            sum_2 += 1
        elif s[i] == "{":
            sum_3 += 1
        elif s[i] == ")":
            sum_4 += 1
        elif s[i] == "]":
            sum_5 += 1
        elif s[i] == "}":
            sum_6 += 1
        else:
            sum_save += 1

    if (sum_1 == sum_4) and (sum_1 != 0 and sum_2 != 0 and sum_3 != 0 and sum_4 != 0 and sum_5 != 0 and sum_6 != 0) and(sum_2 == sum_5) and (sum_3 == sum_6):
        return print("True")
    else:
        return print("False")


if __name__ == "__main__":
    main("((5+3)*2+1)")
    main("{[(3+1)+2]+}")
    main("(3+{1-1)}")
    main("[1+1]+(2*2)-{3/3}")
    main("(({[(((1)-2)+3)-3]/3}-3)")