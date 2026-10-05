def main():
    print("=== Order Approval System ===")
    
    # Input collection
    try:
        order_amount = float(input("Enter total order amount (TRY): "))
        available_stock = int(input("Enter available stock: "))
        requested_quantity = int(input("Enter requested quantity: "))
    except ValueError:
        print("\nError: Please enter valid numeric values for amount, stock, and quantity.")
        return

    is_member_input = input("Is the customer a member? (yes/no): ").strip().lower()
    is_member = is_member_input in ["yes", "y", "true", "1"]

    # Validation: Check for invalid quantities or insufficient stock using logical operators
    if requested_quantity <= 0 or available_stock < 0:
        print("\nResult: Order REJECTED.")
        print("Reason: Invalid quantity or stock values entered.")
    elif requested_quantity > available_stock:
        print("\nResult: Order REJECTED.")
        print("Reason: Insufficient stock available.")
    else:
        # Order is approved
        print("\nResult: Order APPROVED.")
        print(f"Reason: Stock is sufficient (Requested: {requested_quantity}, Available: {available_stock}).")
        
        final_price = order_amount
        
        # Apply 10% discount for members on approved orders of at least 500 TRY (using 'and')
        if is_member and order_amount >= 500.0:
            discount = order_amount * 0.10
            final_price = order_amount - discount
            print(f"Discount applied: 10% member discount (-{discount:.2f} TRY)")
        elif is_member and order_amount < 500.0:
            print("Note: Member discount not applied (order amount is below 500 TRY).")
        else:
            print("Note: Customer is not a member; standard price applies.")
            
        print(f"Final Price: {final_price:.2f} TRY")

if __name__ == "__main__":
    main()
