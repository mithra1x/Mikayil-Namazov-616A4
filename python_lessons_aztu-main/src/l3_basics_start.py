# Dərs 3 · Blok 1 — Python-un 10 kərpici
# İşə salma (de-praktikum qovluğundan): python src/l3_basics_start.py
# Dərsdə hər kərpicin kodunu slayddan öz bölməsinə yazırıq.
# Hər bölmə əvvəlcə öz başlığını çap edir — terminalda həmişə
# ən aşağıdakı bölməyə baxın. Tam kod dərsdən sonra Teams-də olacaq.

print("=== Kərpic 1 ===")   # Proqram — əmrlər ardıcıllığı
print("Salam, data mühəndisliyi!")
print("Baza stansiyası:", "BAK-0207")
print(2 + 3)
print("2 + 3")



print("=== Kərpic 2 ===")
cell = "BAK-0207"   # qutu: adı cell, içində mətn
rsrp = -95.5        # qutu: adı rsrp, içində ədəd
print(cell, rsrp)
rsrp = -108.1       # yeni dəyər qoyduq — köhnəsi itdi
print(cell, rsrp)
drops = 2
drops = drops + 1   # götür, 1 əlavə et, geri qoy
print("drops =", drops)



print("=== Kərpic 3 ===")
print(type(3))           # int — tam ədəd
print(type(-95.5))       # float — kəsr ədəd
print(type("BAK-0207"))  # str — mətn (dırnaq içində)
print(type(True))        # bool — məntiqi: True / False
print(type(None))        # None — «dəyər yoxdur»



print("=== Kərpic 4 ===")
rsrp = -108.1
print(rsrp < -105)        # siqnal -105 dBm-dən zəifdirmi?
print(rsrp > -105)
print(rsrp == -108.1)     # == «bərabərdirmi?» sualıdır
region = "Yasamal"
print(region == "Yasamal")
print(region == "YASAMAL")  # hərf ölçüsü fərqlidir → False



print("=== Kərpic 5 ===")
rsrp_list = [-91.5, -108.1, -86.2, -103.3, -97.4]
print(rsrp_list[0])    # birinci element — indeks 0-dan başlayır
print(rsrp_list[1])    # ikinci element
print(rsrp_list[-1])   # sonuncu element
print(len(rsrp_list))  # elementlərin sayı
avg = sum(rsrp_list) / len(rsrp_list)
print(round(avg, 1))   # orta qiymət



print("=== Kərpic 6 ===")
row = {"cell_id": "BAK-0207", "region": "Yasamal", "rsrp_dbm": -108.1}
print(row["region"])      # açara görə dəyər
print(row["rsrp_dbm"])
row["band"] = "LTE800"    # yeni açar və dəyər əlavə etdik
print(row)



print("=== Kərpic 7 ===")
rsrp_list = [-91.5, -108.1, -86.2, -103.3, -110.4]
weak = 0                  # sayğac: hələ zəif ölçmə yoxdur
for v in rsrp_list:       # hər ölçmə üçün aşağıdakını təkrarla
    if v < -105:          # şərt doğrudursa...
        print(v, "→ zəif")
        weak = weak + 1
    else:                 # ...yoxsa
        print(v, "→ normal")
print("Zəif ölçmə sayı:", weak)



print("=== Kərpic 8 ===")
print(round(-97.36, 1))              # funksiya(arqument, arqument)
print(len("BAK-0207"))               # mətndə neçə simvol var
print(max([-91.5, -108.1, -86.2]))   # ən böyük dəyər
print(round(-97.36, ndigits=1))      # adlı arqument — eyni nəticə



print("=== Kərpic 9 ===")   # Nöqtə: metod
# TODO: name.strip().capitalize()

print("=== Kərpic 10 ===")  # import — hazır alət qutusu
# TODO: import math; import pandas as pd
