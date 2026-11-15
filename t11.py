# -93.2 -107.6 NA -88.4 -101.5 -106.3 NA -96.8 -90.1
# -82.5 -87.3 -92.1 -98.6
# -109.2 -112.4 NA -103.8 -104.2 -118.5 -94.6 NA NA -108.7


def level(signal): # siqnalin ne veziyyetde oldugunu yoxlayir
    if signal < -105:
        return "pis"
    elif signal < -95:
        return "normal"
    else:
        return "ela"


# task 1
melumat = input().split() # daxil edilen reqemleri ayiririq

signals = [] # reqemleri bura yigacagiq
empty = 0 # NA olanlari saymaq ucun

for item in melumat:
    if item == "NA":
        empty += 1 # bos deyer tapdiqda say artir
    else:
        signals.append(float(item)) # reqemi float edib liste elave edirik

print("Ölçü:", len(signals))
print("Boş olanlar:", empty)

# task 2
minimum = min(signals) # en kicik qiymet
maximum = max(signals) # en boyuk qiymet

average = round(sum(signals) / len(signals), 1) # butun reqemleri toplayib sayina boluruk

print("Min:", minimum)
print("Max:", maximum)
print("Ədədi orta:", average)


# task 3
for value in signals:
    result = level(value) # her reqemin hansi qrupa dusduyune baxiriq
    print(value, "-", result)


# task 4
categories = {
    "pis": 0,
    "normal": 0,
    "ela": 0
} # her birinin sayini ayri saxlayiriq

for value in signals:
    category = level(value)
    categories[category] += 1 # hansi qrupa aiddirse onun sayini bir artiririq

print(categories)


# task 5
bad_percent = round(categories["pis"] * 100 / len(signals), 1) # pis siqnallarin faizini tapiriq

print("pis gosterici:", bad_percent, "%")

if bad_percent >= 30:
    print("texniki heyete xeber verilsin") # veziyyet pisdir
elif bad_percent >= 10:
    print("monitorinq davam etsin") # veziyyete nezaret etmek lazimdir
else:
    print("stansiya normal isleyir") # ciddi problem yoxdur


# task 6
current = 0 # ard-arda gelen pis siqnallarin sayi
longest = 0 # en cox nece defe tekrarlandigini saxlayir

for value in signals:
    if level(value) == "pis":
        current += 1 # pis siqnal geldikce sayi artir
        longest = max(longest, current) # en boyuk ardicil sayi yadda saxlayiriq
    else:
        current = 0 # pis siqnal kesilende sayi sifirlayiriq
