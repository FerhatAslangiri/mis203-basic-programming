# Lab Quiz: Savings Planner

## Test Run
- **Test Inputs:** Starting Balance = 1000, Monthly Deposit = 500, Monthly Rate = 1%, Savings Goal = 3000
- **Expected Result:** Reached in 4 months, Final Balance = 3070.80, Total Interest = 70.80.
- **Outcome:** Passed successfully.

## Changes After Testing
- Added a helper function (`get_input`) with a `while` loop and `try-except` block to validate user inputs cleanly and
-  avoid code repetition for negative/non-numeric checks.
