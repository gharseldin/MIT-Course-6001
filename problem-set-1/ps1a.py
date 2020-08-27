annual_salary = float(input("Enter your annual salary : "))
portion_saved = float(
    input("What percentage will you save from your salary? : "))
total_cost = float(input("What is the price of the house? : "))

# first we calculate the amount of the down payment
portion_down_payment = 0.25 * total_cost

# initialize savings to zero
current_savings = 0

# initialize monthly return on savings rate
monthly_rate = 0.04 / 12

# initialize the total time we have spent saving. Zero so far
saving_time = 0

# start looping until we make the portion for the down payment
while current_savings < portion_down_payment:
    monthly_return = current_savings * monthly_rate
    monthly_savings = portion_saved * annual_salary / 12
    current_savings += monthly_return + monthly_savings
    saving_time += 1

print("-----------------------------------")
print("Time spent saving =", saving_time, "months")
print("That is", int(saving_time/12), "years, and", saving_time % 12, "months")
