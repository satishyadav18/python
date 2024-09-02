import matplotlib.pyplot as plt

# Take user input for five marks
marks = [95, 59, 87, 79, 84]

# Define labels for the bars
labels = ['Mark 1', 'Mark 2', 'Mark 3', 'Mark 4', 'Mark 5']

# Create a bar chart
plt.bar(labels, marks, color='blue')

# Add labels and title
#plt.xlabel('Marks')
plt.ylabel('Score')
plt.title('Student Marks for a Subject')

# Display the plot
plt.show()
