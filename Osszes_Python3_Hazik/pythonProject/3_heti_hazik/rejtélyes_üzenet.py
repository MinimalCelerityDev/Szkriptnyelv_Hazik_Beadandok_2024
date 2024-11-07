text="""
    Cbcq Dgyk!

    Dmeybh kce cew yrwyg hmrylyaqmr:
    rylsjb kce y Nwrfml npmepykmxyqg lwcjtcr!

    Aqmimjjyi:

    Ynyb    
    """
def main():
    result = text.replace('k', 'm').\
        replace('l','n').replace('m','o').\
        replace('n','p').replace('j','l').\
        replace('f','h').replace('g','i').\
        replace('h','j').replace('i','k').\
        replace('j','l').replace('a','c').\
        replace('b','d').replace('c','e').\
        replace('d','f').replace('e','g').\
        replace('o','q').replace('p','r').\
        replace('q','s').replace('r','t').\
        replace('s','u').replace('t','v').\
        replace('u','w').replace('v','x').\
        replace('w','a').replace('x','b')

    return print(result)

if __name__ == "__main__":
    main()
