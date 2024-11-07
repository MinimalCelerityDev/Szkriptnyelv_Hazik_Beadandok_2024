def trukkos_tunteto():
    bin1 = "01111001";
    bin2 = "01110101";
    bin3 = "01110101";
    bin4 = "01100010";
    bin5 = "00101111"
    bin6 = "01010001";
    bin7 = "00110100";
    bin8 = "00111001";
    bin9 = "01100111";
    bin10 = "01100011"
    bin11 = "01101111";
    bin12 = "01110100";
    bin13 = "00101110";
    bin14 = "01100101";
    bin15 = "01100100"
    bin16 = "01110111";
    bin17 = "01110111";
    bin18 = "01010111";
    bin19 = "01011000";
    bin20 = "01010001"

    text = chr(int(bin1, 2)) + chr(int(bin11, 2)) + chr(int(bin2, 2)) + chr(int(bin12, 2)) + chr(int(bin3, 2)) + chr(
        int(bin13, 2)) + chr(int(bin4, 2)) + chr(int(bin14, 2)) + chr(int(bin5, 2)) + chr(int(bin15, 2)) + chr(
        int(bin6, 2)) + chr(int(bin16, 2)) + chr(int(bin7, 2)) + chr(int(bin17, 2)) + chr(int(bin8, 2)) + chr(
        int(bin18, 2)) + chr(int(bin9, 2)) + chr(int(bin19, 2)) + chr(int(bin10, 2)) + chr(int(bin20, 2))
    print(text)


def apple():
    TEXT = """
    01010011 01101111 00100000 01111001 01101111 01110101 00100000 01110100 01101111 01101111 01101011
    00100000 01110100 01101000 01100101 00100000 01110100 01101001 01101101 01100101 00100000 01110100
    01101111 00100000 01110100 01110010 01100001 01101110 01110011 01101100 01100001 01110100 01100101
    00100000 01110100 01101000 01101001 01110011 00111111 00100000
    01010111 01100101 00100000 01101100 01101111 01110110 01100101 00100000 01111001 01101111 01110101
    00101110"""

    felbontott = TEXT.split()
    for i in range(len(felbontott)):
        print(chr(int(felbontott[i], 2)), end="")


def legkeresettebb_hacker():
    MY_TEXT = """4D69 61 6E657665 616E6E616B 61 68656C7969
    6B617063736F6C6F6B6F7A706F6E746E616B2C 61686F6C
    6D616A646E656D 656C6B617074616B"""

    print("\n")
    felbontott_text = MY_TEXT.split()
    for i in range(len(felbontott_text)):
        felbontott_text[i] = felbontott_text[i].zfill(38)
        print(bytes.fromhex(felbontott_text[i]).decode('utf-8'), end=" ")


if __name__ == "__main__":
    trukkos_tunteto()
    apple()
    legkeresettebb_hacker()