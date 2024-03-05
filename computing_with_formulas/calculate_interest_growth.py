interest_rate = 1.72  # percent

def calculate_growth(initial_amount, interest_rate, years):
    # Convert interest rate to decimal
    interest_rate_decimal = interest_rate / 100

    # Calculate growth amount
    growth_amount = initial_amount * (1 + interest_rate_decimal) ** years

    return growth_amount

# Initial amount
initial_amount = 1000  # dollars

# Calculate growth amount after three years
growth_amount = calculate_growth(initial_amount, interest_rate, 3)

# Print out the results
print(f"Initial amount: ${initial_amount}")
print(f"Interest rate: {interest_rate}%")
print(f"Growth amount after three years: ${growth_amount:}")