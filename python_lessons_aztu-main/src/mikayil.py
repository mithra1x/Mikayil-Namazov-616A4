# # Dərs 3 · Blok 1 — Python-un 10 kərpici
# # İşə salma (de-praktikum qovluğundan): python src/l3_basics_start.py
# # Dərsdə hər kərpicin kodunu slayddan öz bölməsinə yazırıq.
# # Hər bölmə əvvəlcə öz başlığını çap edir — terminalda həmişə
# # ən aşağıdakı bölməyə baxın. Tam kod dərsdən sonra Teams-də olacaq.

# print("=== Kərpic 1 ===")   # Proqram — əmrlər ardıcıllığı
# # TODO: print(...) ilə 4 sətir (slayd «Kərpic 1»)

# # print ("SALAM, menim ad!")
# # print ("BAZA STANSIYASI: ", "bak-0207")
# # print(4+4)
# # print("4+4")

# print("=== Kərpic 2 ===")   # Dəyişən — adı olan qutu
# # TODO: cell, rsrp, drops

# # cell = "ad"
# # rsrp = -95.5

# # print(cell,rsrp)

# # rsrp = -108.1

# # print(cell,rsrp)

# # drops = 2
# # drops = drops +1
# # print ("drops =", drops)


# print("=== Kərpic 3 ===")   # Tiplər: int, float, str, bool, None
# # TODO: type(...) və «mətn ≠ ədəd»

# # print(type(3))
# # print(type(-95.5))
# # print(type("bak-0207"))
# # print(type(True))
# # print(type(None))
# # ad= input()
# # yas = input()
# # qrup ="616.a2"
# # print("Salam menim adim:",ad, " ve menim",yas, "gelen il olacaq", "qrupum ise budur:", qrup)

# ad = str(input("AD: "))
# yas = int( input("YAS: "))
# qrup = input("qrup: ")

# print("Salam menim adim:", ad, "ve menim", yas, "yasim var. qrupum ise budur:", qrup)




# print("=== Kərpic 4 ===")   # Müqayisə → True / False
# # TODO: rsrp < -105, ==
# print( yas > 20 )
# print(ad==Kanan)


# print("=== Kərpic 5 ===")   # Siyahı (list)
# # TODO: rsrp_list, indeks, len, orta

print("=== Kərpic 6 ===")   # Lüğət (dict)
# # TODO: row = {...}, row["region"]

# row = {
#     "cell_id": "BAK-050",
#     "region": " SUMGAIT",
#     "rsrp_dmb": -11.1}

# print(row["region"])
# row["region"] = "MERDEKAN"
# print(row["region"])

# x = input("deyisikliyi daxzil edin: ")
# row["region"] = x
# print(row["region"])

# print(row)

#-------------------------------
# key = input("Acari daxil et: ")
# print(row)
# value = input("deyismek istediyivi daxil et ")
# row[key] = value

# print(row[key])


print("=== Kərpic 7 ===")   # Dövr (for) və şərt (if / else)
# TODO: zəif ölçmələri saymaq

rsps_list = [981, 1, 126, 12]


for b in rsps_list:
    a =int( input ("ededivi daxil et: "))
    print(b *a)

print("=== Kərpic 8 ===")   # Funksiya: çağırmaq və yaratmaq
# TODO: round, len, max; def is_weak(rsrp)

print("=== Kərpic 9 ===")   # Nöqtə: metod
# TODO: name.strip().capitalize()

print("=== Kərpic 10 ===")  # import — hazır alət qutusu
# TODO: import math; import pandas as pd
