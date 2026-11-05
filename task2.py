days = ["Sun", "Mon", "Tue", "Wed", "Thu"]
sales = [1200, 950, 1800, 1430, 2100]

total = 0
best_sale = 0
best_day = ""
above_target = 0

for i in range(len(sales)):
    print(f"{days[i]}: {sales[i]} SAR")
    total = total + sales[i]
    if sales[i] > best_sale:
        best_sale = sales[i]
        best_day = days[i]
    if sales[i] > 1500:
        above_target = above_target + 1

average = total // len(sales)

print(f"Total: {total} SAR")
print(f"Average: {average} SAR")
print(f"Best day: {best_day} ({best_sale} SAR)")
print(f"Days above target: {above_target}")


# نحتاج رقم اليوم (i) عشان نوصل لاسم اليوم ومبيعاته مع بعض، و for s in sales يعطينا المبيعات بس بدون الاسم.