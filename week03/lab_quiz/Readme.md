# Lab 03 - Order Approval Policy

## Test Table (Boundary Cases)

| Case Description | Order Amount (TRY) | Available Stock | Requested Quantity | Is Member? | Expected Result |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Just below 500 TRY** | 499.00 | 10 | 2 | Yes | Approved, Reason shown, Final Price: 499.00 TRY (No discount) |
| **Exactly at 500 TRY** | 500.00 | 10 | 2 | Yes | Approved, Reason shown, Final Price: 450.00 TRY (10% discount applied) |
| **Above 500 TRY** | 600.00 | 10 | 2 | Yes | Approved, Reason shown, Final Price: 540.00 TRY (10% discount applied) |
| **Insufficient Stock** | 550.00 | 5 | 10 | Yes | Rejected, No final price shown |

## Development Notes

* **Test Run:** Tested with an order amount of 500 TRY, 10 stock, 2 requested items, and member status set to "yes".
* The program correctly applied the 10% discount and output a final price of 450.00 TRY.
* **Change Made After Testing:** Initially, the script didn't handle invalid string inputs (like letters instead of numbers), which caused a crash.
* Added a `try-except` block to catch `ValueError` and safely exit with an error message.
