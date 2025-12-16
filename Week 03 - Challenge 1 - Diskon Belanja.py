# Function to calculate total price after discount
def calculate_total(price, quantity, discount=0):
    total = price * quantity                # Calculate total price before discount
    total -= total * (discount / 100)       # Subtract discount from total price
    return total                            # Return final price after discount

# Print header
print("=======================================")
print("======== DISCOUNT CALCULATOR ==========")
print("=======================================")
print("")

# Get user input for price, quantity, and discount
price = int(input("Enter item price: "))         # Input item price
quantity = int(input("Enter item quantity: "))   # Input item quantity
discount = int(input("Enter discount (%): "))    # Input discount percentage

# Calculate total shopping amount
total_purchase = calculate_total(price, quantity, discount)

# Print the result
print(f"Total purchase = Rp{total_purchase:,.0f}")
