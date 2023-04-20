import matplotlib.pyplot as plt

# Data
years = ['Year 0', 'Year 1', 'Year 2', 'Year 3']
units_sold = [80, 100, 115, 125]
total_revenue = [332150, 415188, 477466, 518985]
total_expenses = [291356, 286906, 295543, 304401]
profit_losses = [40794, 128282, 181923, 214584]

# Plot the data
plt.plot(years, total_revenue, label='Total Revenue', marker='o')
plt.plot(years, total_expenses, label='Total Expenses', marker='o')
plt.plot(years, profit_losses, label='Profit/Losses', marker='o')

# Customize the graph
plt.xlabel('Years')
plt.ylabel('Amount ($)')
plt.title('Financial Overview')
plt.legend()

# Show the graph
plt.show()

