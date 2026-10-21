import pandas as pd
l=[1,2,3,4,5,6,7,8,9,11,11,12,13,15,17,20]
target=int(input())
left = 0
right = len(l) - 1
found_index = -1

while left <= right:
  mid = (left + right) // 2

  if l[mid] == target:
    found_index = mid
    break
  elif l[mid] < target:
    left = mid + 1
  else:
    right = mid - 1

if found_index != -1:
  print(f"Ədəd tapildi! İndeksi: {found_index}")
else:
  print("Ədəd siyahida yoxdur.")
