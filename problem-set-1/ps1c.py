annual_salary = float(input("Enter your annual salary : "))
total_cost = 1000000
semi_annual_raise = 0.07

# calculate the amount of the down payment
portion_down_payment = 0.25 * total_cost

# initialize savings to zero
current_savings = 0

# initialize monthly return on savings rate
monthly_rate = 0.04 / 12

# initialize a tuple of range to use for bisections
# our range is from 0% to 100%
# if we save 0% we will reach our target in infinity months
# if we save 100% we will reach our target down payment at the lowest no. of months.
range = (0, 1)

# if our salary is very low and maximum time is more than 36 months then there is nothing
# we can do to save the money in 36 months. Let's handle that case first
# start looping until we finish 36 months to see the max we can save in 36 months with interest
saving_time = 0
iteration_annual_salary = annual_salary

while saving_time != 36:
    saving_time += 1
    monthly_return = current_savings * monthly_rate
    monthly_savings = iteration_annual_salary / 12
    current_savings += monthly_return + monthly_savings
    if saving_time % 6 == 0:
        iteration_annual_salary += iteration_annual_salary * semi_annual_raise

if current_savings < portion_down_payment:
    print("-----------------------------------")
    print("It is not possible to pay the down payment in three years")

# else if its doable
else:
    # keep looping indefinitely until you get the the rate
    # that will get us there in 36 months
    # we also need to keep track of number of iterartions
    iterations = 0
    while (True):

        iterations += 1

        # reset salary and savings to original numbers for each iteration
        # since we adjust them in our calculations
        iteration_annual_salary = annual_salary
        current_savings = 0
        saving_time = 0

        # bisect
        portion_saved = range[0] + (range[1] - range[0])/2

        # start looping until we make the portion for the down payment
        while current_savings < portion_down_payment:
            saving_time += 1
            monthly_return = current_savings * monthly_rate
            monthly_savings = portion_saved * iteration_annual_salary / 12
            current_savings += monthly_return + monthly_savings
            if saving_time % 6 == 0:
                iteration_annual_salary += iteration_annual_salary * semi_annual_raise

        # if time is less than 36 it was too fast, we need to save less
        # so this rate becomes the upper limit in the tuple
        if saving_time < 36:
            range = (range[0], portion_saved)
            # we do it this way because tuples are not mutable

        # if time is greater than 36 then we need to save more.
        # so since this rate was not enough it becomes our lower limit in the tuple
        elif saving_time > 36:
            range = (portion_saved, range[1])

        # if its not less than or greater than 36 then it must be equal to 36
        # in that case we have our saveing rate which is the mid point of the current range
        # #trying to add more granuality here to achieve 100$ threshold
        else:
            if current_savings - portion_down_payment > 100:
                range = (range[0], portion_saved)
            else:
                break

    print("-----------------------------------")
    print("Best savings rate:", range[0] + (range[1]-range[0])/2)
    print("Steps in bisection search:", iterations)
