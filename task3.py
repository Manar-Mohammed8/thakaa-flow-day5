def add_vat(amount, rate=0.15):
    return round(amount * (1 + rate), 2)


def format_price(amount):
    return f"{amount:,.2f} SAR"


def is_valid_phone(phone):
    phone = phone.replace(" ", "")
    if len(phone) == 10 and phone.startswith("05") and phone.isdigit():
        return True
    return False


# اختبار add_vat
print(add_vat(100))
print(add_vat(500))
print(add_vat(1000))

# اختبار format_price
print(format_price(1234.5))
print(format_price(100))
print(format_price(50.75))

# اختبار is_valid_phone
print(is_valid_phone("0551234567"))
print(is_valid_phone("05512"))
print(is_valid_phone("05abc12345"))

# استخدام الدوال معًا
print(format_price(add_vat(1000)))

# فحص الارقام
phones = [
    "0551234567",
    "0661234567",
    "055 123 4567",
    "05512",
    "05abc12345"]

count = 0

for phone in phones:
    if is_valid_phone(phone):
        print(phone)
        count += 1

print(f"Valid phones: {count}")
