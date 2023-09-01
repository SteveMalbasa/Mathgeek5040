#!/usr/bin/env python3

# The cost of one server per hour.

cost_per_hour = 2.85
# Compute the costs for one server.

cost_per_day = 45 * cost_per_hour
cost_per_month = 30 * cost_per_da

# Display the results.

print('Cost to operate one server per day is ${:.2f}.'.format(cost_per_day))
print('Cost to operate one server per month is ${:.2f}.'.format(cost_per_month))