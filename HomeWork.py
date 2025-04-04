# Problem: Determine the best savings rate (r) to afford the down payment in 36 months using bisection search
###Problem From MIT ###
# Inputs
total_cost = 750000
portion_down_payment = 0.25
down_payment = total_cost * portion_down_payment
annual_return = 0.04
months = 36

# User savings
starting_savings = float(input("Enter your current savings: "))
monthly_salary = float(input("Enter your monthly salary: "))

# Define bisection search parameters
epsilon = 100  # acceptable margin
low = 0.0
high = 1.0
steps = 0
best_rate = None

# Check if it's even possible
max_savings = 0
current_savings = 0
for month in range(1, months + 1):
    current_savings += (monthly_salary * high)
    current_savings += current_savings * (annual_return / 12)
    max_savings = current_savings

if max_savings < down_payment - epsilon:
    print("It is not possible to afford the down payment in 36 months.")
else:
    while True:
        steps += 1
        guess = (low + high) / 2
        current_savings = 0

        for month in range(1, months + 1):
            current_savings += (monthly_salary * guess)
            current_savings += current_savings * (annual_return / 12)

        if abs(current_savings - down_payment) <= epsilon:
            best_rate = guess
            break
        elif current_savings < down_payment:
            low = guess
        else:
            high = guess

    print(f"Best savings rate: {round(best_rate, 4)}")
    print(f"Steps in bisection search: {steps}")