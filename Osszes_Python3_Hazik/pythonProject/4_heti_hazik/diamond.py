def diamond(magassagossag):

    if magassagossag % 2 == 0:
        print("Itt muszáj páratlan legyen a dolog")
        return

    for i in range(1, magassagossag, 2):
        print(("*" * i).center(magassagossag))

    print("*" * magassagossag)

    for i in range(magassagossag - 2, 0, -2):
        print(("*" * i).center(magassagossag))

if __name__ == "__main__":
    diamond(3)
    diamond(7)
