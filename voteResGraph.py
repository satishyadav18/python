


import matplotlib.pyplot as plt

# Election results data
parties = ['ABC', 'XYZ', 'MNP']
seats = [180, 200, 400 - (180 + 200)]  # Seats for 'MNP' is calculated as the remaining seats

# Create a bar chart
plt.bar(parties, seats)
#''', color=['blue', 'green', 'red'])'''

# Add labels and title
plt.xlabel('Parties')
plt.ylabel('Number of Seats')
plt.title('Election Results - India 2000')

# Display the bar chart
plt.show()
