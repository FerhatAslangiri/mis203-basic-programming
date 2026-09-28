# Lab 02: Purchase Quote Calculator

This Python script (`lab02_purchase_quote.py`) calculates a custom two-item purchase quote. It takes item names, quantities, unit prices, delivery fees, 
and tax percentages as inputs, computes the subtotal, applies taxes and delivery, and prints a formatted summary receipt.

## Test Run

I tested the program with the required sample values:
- **Item 1:** Quantity = 2, Unit Price = 50.00 TRY
- **Item 2:** Quantity = 1, Unit Price = 80.00 TRY
- **Delivery Fee:** 20.00 TRY
- **Tax Percentage:** 10%

**Expected Result:** 218.00 TRY  
**Actual Result:** 218.00 TRY (Verified successfully)

## Change Made After Testing

After running the initial test, I noticed that the decimal alignments in the receipt summary looked slightly off when prices had different digit lengths.
I updated the f-string formatting (e.g., using explicit spacing and `:.2f`) to ensure all the TRY amounts align neatly on the right side of the output terminal.
