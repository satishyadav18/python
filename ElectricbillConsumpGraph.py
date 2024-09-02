'''Display electricity consumption of a customer for 12 months using suitable
graphical tools.'''


import matplotlib.pyplot as plt
import random

months = ['jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul', 'aug', 'sep', 'oct', 'nov', 'dec']
consumption = []
for i in range(12):
    consumption.append(random.randint(300, 1000))

plt.bar(months, consumption)
plt.show()