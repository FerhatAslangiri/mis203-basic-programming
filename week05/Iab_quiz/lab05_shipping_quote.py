# lab05_shipping_quote.py

def calculate_subtotal(unit_price, quantity):
    """Birim fiyat ve miktara göre ara toplamı hesaplar."""
    return unit_price * quantity

def calculate_discount_rate(subtotal):
    """Ara toplama göre indirim oranını belirler (Eşik sınır: 500)."""
    if subtotal >= 500:
        return 0.10  # %10 indirim
    return 0.0     # İndirim yok

def calculate_shipping_fee(subtotal):
    """Ara toplama göre kargo ücretini belirler (Eşik sınır: 300)."""
    if subtotal >= 300:
        return 0.0   # Ücretsiz kargo
    return 50.0    # Standart kargo ücreti

def calculate_final_total(subtotal, discount_rate, shipping_fee):
    """İndirim ve kargo ücretini hesaba katarak nihai toplamı hesaplar."""
    discounted_amount = subtotal * (1 - discount_rate)
    return discounted_amount + shipping_fee


# --- Kabul Kontrolleri (Assert Checks & Sınır Testleri) ---
# 1. Ara toplam hesaplama testi
assert calculate_subtotal(100, 3) == 300, "Ara toplam hesaplaması hatalı!"

# 2. İndirim eşik sınırı testi (500 sınır değeri: altı ve üstü)
assert calculate_discount_rate(499) == 0.0, "500 altı indirim sınırı hatalı!"
assert calculate_discount_rate(500) == 0.10, "500 üstü/eşit indirim sınırı hatalı!"

# 3. Kargo eşik sınırı testi (300 sınır değeri)
assert calculate_shipping_fee(299) == 50.0, "300 altı kargo sınırı hatalı!"
assert calculate_shipping_fee(300) == 0.0, "300 üstü/eşit kargo sınırı hatalı!"

print("Tüm assert testleri başarıyla geçti!\n")


# --- Örnek Siparişler ---
def process_order(order_id, price, quantity):
    print(f"--- Sipariş #{order_id} ---")
    subtotal = calculate_subtotal(price, quantity)
    discount_rate = calculate_discount_rate(subtotal)
    shipping_fee = calculate_shipping_fee(subtotal)
    final_total = calculate_final_total(subtotal, discount_rate, shipping_fee)
    
    print(f"Ara Toplam: ₺{subtotal:.2f}")
    print(f"İndirim Oranı: {discount_rate * 100}%")
    print(f"Kargo Ücreti: ₺{shipping_fee:.2f}")
    print(f"Nihai Tutar: ₺{final_total:.2f}\n")

# Fonksiyonları en az iki farklı örnek sipariş için çağırıyoruz
process_order(1, 120, 2)  # Ara toplam: 240 (300'ün altında -> kargo var, indirim yok)
process_order(2, 250, 3)  # Ara toplam: 750 (500 ve 300'ün üstünde -> indirim var, kargo bedava)
