import json

def keresem_a_betuket_cuccos(keresem_a_betuket):
    szamolok_hogy_szamoljak = 0



    keresett_betuk = ['j', 's', 'u', 'n']


    for i in keresem_a_betuket:

        if i == keresett_betuk[szamolok_hogy_szamoljak]:

            szamolok_hogy_szamoljak += 1

            if szamolok_hogy_szamoljak == len(keresett_betuk):

                return True

    return False

with open("C:\\Users\\balog1sebas209\\Contacts\\python\\pythonProject\\szoveg.txt", "r") as f:
    sorok = f.readlines()

hany_darabot_talaltunk = []

for i in sorok:
    if keresem_a_betuket_cuccos(i):
        hany_darabot_talaltunk.append(i.strip())

with open("C:\\Users\\balog1sebas209\\Contacts\\python\\pythonProject\\szoveg_megoldva.json", "w") as json_file:
    json.dump(hany_darabot_talaltunk, json_file, indent=4)
