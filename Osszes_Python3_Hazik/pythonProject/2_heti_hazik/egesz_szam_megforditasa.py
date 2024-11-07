def egesz_szam_megforditas_elso_fele_képpen(s):
    s_stringbe = str(s)
    s_stringbe_megforditva = s_stringbe[::-1]
    s_vissszaforditva_egesz_szamba = int(s_stringbe_megforditva)
    return s_vissszaforditva_egesz_szamba

print(egesz_szam_megforditas_elso_fele_képpen(1977))
print(egesz_szam_megforditas_elso_fele_képpen(12568))