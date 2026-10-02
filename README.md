# Mis203 Basic Programming

## Week 01
- **Student Name:** Ferhat Aslangiri
- **Student ID:** 2404109037
- **Department:** Management Information Systems
- **Course:** Basic Programming
- **AI Tool Used:** Gemini
- **Prompt Used:** "Python ile kullanıcıdan isim, bölüm, yaş ve kariyer hedefi alıp ekrana düzenli bir öğrenci profili bastıran basit bir kod yazar mısın?"
- **What did you change?** Girdi alırken değişken isimlerini kendi projemin akışına göre uyarladım ve çıktının ödev formatına tam uyması için print kısımlarını düzenledim.

## Week 02
- **AI Tool Used:** Gemini
- **Prompt Used:** .Python'da sonsuz döngüyle çalışan bir öğrenci not hesaplama programı yazıyorum. Kullanıcı yanlışlıkla sayı yerine harf girerse programın çökmesini nasıl engellerim ve genel ortalamayı virgülden sonra sadece 2 basamak olacak şekilde nasıl yuvarlayabilirim?" diye sordum.
- **What did you change?** Kodun hata vermemesi için sayı dönüşümlerini ekledim ve çıktı formatını yönergeye göre düzenledim.
- **What does break do in your program?** Kullanıcı çıkmak için "q" harfine bastığında sonsuz döngüyü (while döngüsünü) anında sonlandırır.

## Week 03
- **AI Tool Used:** Gemini
- **Prompt Used:** Create a Python program named ticket_office.py that sells cinema tickets with input validation, conditions, loops, and summary statistics according to assignment rules.
- **What did you change?** Added robust input validation using try-except blocks and loops for age, day, and student status, and structured the discount logic using an ordered if-elif-else chain.
- **Tests:**
  1. Input: Name: Zeynep, Age: 5, Day: weekday, Student: no -> Result: Zeynep: 0.00 TRY (Free) *(Boundary age test)*
  2. Input: Name: Ali, Age: 10, Day: weekend, Student: yes -> Result: Ali: 150.00 TRY (Child)
  3. Input: Name: Mehmet, Age: 22, Day: weekday, Student: yes -> Result: Mehmet: 140.00 TRY (Student)
- **Why does the order of the rules matter?** 
  The order matters because Python evaluates conditional statements (`if-elif-else`) sequentially from top to bottom and stops at the first match. If the Student rule came before the Child rule, a 10-year-old student would be incorrectly categorized as a Student (30% discount) instead of a Child (40% discount).
