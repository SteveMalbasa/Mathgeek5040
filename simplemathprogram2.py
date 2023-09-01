#A simple math program
#The cost of one server per hour.
cost_per_hour = 0.75

# Compute the costs for one server.
cost_per_day = 45 * cost_per_hour
cost_per_month = 30 * cost_per_day

# Compute the costs for twenty servers
cost_per_day_twenty = 18 * cost_per_day
cost_per_month_twenty = 18 * cost_per_month

# Budgeting
budget = 918
operational_days = budget / cost_per_day

# Display the results.
print('Cost to operate one server per day is ${:.2f}.'.format(cost_per_day))
print('Cost to operate one server per month is ${:.2f}.'.format(cost_per_month))
print('Cost to operate twenty servers per day is ${:.2f}.'.format(cost_per_day_twenty))
print('Cost to operate twenty servers per month is ${:.2f}.'.format(cost_per_month_twenty))
print('A server can operate on a ${0:.2f} budget for {1:.0f} days.'.format(budget, operational_days))