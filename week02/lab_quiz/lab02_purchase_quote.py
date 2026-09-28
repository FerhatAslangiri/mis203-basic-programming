print("Purchase Quote Calculator")
print("-" * 30)

# 1. Item 1 Bilgileri
item1_name = input("Item 1 name: ").strip()
item1_qty = int(input(f"Quantity for {item1_name}: "))
item1_price = float(input(f"Unit price for {item1_name} (TRY): "))

# 2. Item 2 Bilgileri
item2_name = input("Item 2 name: ").strip()
item2_qty = int(input(f"Quantity for {item2_name}: "))
item2_price = float(input(f"Unit price for {item2_name} (TRY): "))

# 3. Teslimat ve Vergi Bilgileri
delivery_fee = float(input("Delivery fee (TRY): "))
tax_percentage = float(input("Tax percentage (e.g., 10 for 10%): "))

# 4. Hesaplamalar
line1_total = item1_qty * item1_price
line2_total = item2_qty * item2_price
subtotal = line1_total + line2_total

tax_amount = subtotal * (tax_percentage / 100)
final_total = subtotal + tax_amount + delivery_fee

# 5. Raporlama ve Çıktı
print()
print("=" * 45)
print(" PURCHASE QUOTE SUMMARY")
print("=" * 45)
print(f"1. {item1_qty}x {item1_name} @ {item1_price:.2f} TRY = {line1_total:.2f} TRY")
print(f"2. {item2_qty}x {item2_name} @ {item2_price:.2f} TRY = {line2_total: .2f} TRY")
print("-" * 45)
print(f"Subtotal:       {subtotal:10.2f} TRY")
print(f"Tax ({tax_percentage:.0f}%):    {tax_amount:10.2f} TRY")
print(f"Delivery Fee:   {delivery_fee:10.2f} TRY")
print("=" * 45)
print(f"FINAL TOTAL:    {final_total:10.2f} TRY")
print("=" * 45)
