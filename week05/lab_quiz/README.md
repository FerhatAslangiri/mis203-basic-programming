# Lab 05 - Shipping Quote

## Test Edilen Senaryo
* **Test:** 250 TL'lik üründen 3 adet alınarak toplam 750 TL'lik bir sipariş oluşturuldu. 
* **Sonuç:** Ara toplam 500 TL'yi aştığı için %10 indirim uygulandı ve 300 TL sınırını geçtiği için kargo ücreti 0 TL (ücretsiz) olarak hesaplandı. Assert testleri ve sınır değerleri (500 TL ve 300 TL eşikleri) başarıyla doğrulandı.

## Test Sonrası Yapılan Değişiklik
* **Değişiklik:** İlk kod tasarımında indirim eşiği sadece büyük (`> 500`) olarak yazılmıştı. Sınır testleri (boundary testing) sırasında tam 500 TL tutarındaki siparişlerin indirim almadığını fark edip koşulu büyük veya eşit (`>= 500`) olarak güncelledim.
