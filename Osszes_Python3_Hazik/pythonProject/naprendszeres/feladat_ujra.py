import re
import json

#internetes_kis_segitseg

def keres_j_s_u_n(line):
    minta = r"J.*S.*U.*N"
    return bool(re.search(minta, line, re.IGNORECASE))

with open("C:\\Users\\balog1sebas209\\Contacts\\python\\pythonProject\\szoveg.txt", "r") as f:
    sorok = f.readlines()

talalatok = []
for sor in sorok:
    if keres_j_s_u_n(sor):
        talalatok.append(sor.strip())

with open("C:\\Users\\balog1sebas209\\Contacts\\python\\pythonProject\\szoveg_megoldva.json", "w") as json_file:
    json.dump(talalatok, json_file, indent=4)
