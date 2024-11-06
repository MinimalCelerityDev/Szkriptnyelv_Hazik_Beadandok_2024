import sys

ez_lesz_a_skript_neve = sys.argv[0]

if "z-a" in ez_lesz_a_skript_neve:

    print("".join(chr(c) for c in range(ord('z'), ord('a') - 1, -1)))

else:

    print("".join(chr(c) for c in range(ord('a'), ord('z') + 1)))
