annual_salary = float(input("Enter your annual salary : "))
portion_saved = float(
    input("What percentage will you save from your salary? : "))
total_cost = float(input("What is the price of the house? : "))
semi_annual_raise = float(input("What is your semi-annual raise? : "))

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
    saving_time += 1
    monthly_return = current_savings * monthly_rate
    monthly_savings = portion_saved * annual_salary / 12
    current_savings += monthly_return + monthly_savings
    if saving_time % 6 == 0:
        annual_salary += annual_salary * semi_annual_raise

print("-----------------------------------")
print("Time spent saving =", saving_time, "months")
print("That is", int(saving_time/12), "years, and", saving_time % 12, "months")
