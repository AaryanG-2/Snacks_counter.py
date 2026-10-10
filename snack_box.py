snack_box1 = {"juice", "chips","sandwhich", "fruits"}
snack_box2 = {"soda", "cookies","sandwhich", "fruits"}
print(snack_box1)
print(snack_box2)
snack_box1.add("banana")
print(snack_box1)
common_snacks = snack_box1.intersection(snack_box2)
print(f"Snacks in both boxes = {common_snacks}")

import array as arr
snacks_counts = arr.array("i", [4,1,2,3])
print(f"Snacks count = {snacks_counts}")
snacks_counts.insert(0,5)
snacks_counts.append(6)
print(f"Array after adding items: {snacks_counts}")
count_of_2 = snacks_counts.count(2)
reversed_snack_counts = snacks_counts.reverse
print(f"Reversed snacks counts = {reversed_snack_counts}")

print("")
print("========================================")
print("Snack box 1 = ",snack_box1)
print("Snack box 2 = ",snack_box2)
print(f"Shared snacks = {common_snacks}")
print(f"Num of snacks = {snacks_counts}")
print("========================================")