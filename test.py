row = {"Baki": "77", "Gence":"20" }
print("First")
print(row["Baki"])

print("Changed:")
row["Baki"] = "10"
print(row["Baki"])

deyis = input("Change:")

row["Gence"] = deyis
print(row["Gence"])
print(row)
"""
--------"""
key = input("Acar: ")
print(row)
value = input("daxil et ")
row[key] = value

print(row[key])