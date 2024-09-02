#B) Display the marks of two students for 5 subjects using suitable graphical tools.
'''
import matplotlib.pyplot as plt
import numpy as np

# Student names
students = ['Student 1', 'Student 2']

# Subject names
subjects = ['Subject 1', 'Subject 2', 'Subject 3', 'Subject 4', 'Subject 5']

# Marks for each student in each subject
marks_student1 = [85, 90, 78, 88, 92]
marks_student2 = [78, 85, 80, 92, 88]

# Set up positions for bars on X-axis
bar_width = 0.35
index = np.arange(len(subjects))

# Create bar plots for each student
plt.bar(index, marks_student1, width=bar_width, label='Student 1')
plt.bar(index + bar_width, marks_student2, width=bar_width, label='Student 2')

# Set labels and title
plt.xlabel('Subjects')
plt.ylabel('Marks')
plt.title('Marks of Two Students for 5 Subjects')
plt.xticks(index + bar_width / 2, subjects)
plt.legend()

# Show the plot
plt.show()

//////////
'''

import matplotlib.pyplot as plt
import numpy as np

# Student names
students = ['Student 1', 'Student 2']

# Subject names
subjects = ['Subject 1', 'Subject 2', 'Subject 3', 'Subject 4', 'Subject 5']

# Marks for each student in each subject
marks_student1 = [85, 90, 78, 88, 92]
marks_student2 = [78, 85, 80, 92, 88]

# Set up positions for bars on X-axis
bar_width = 0.35
index = np.arange(len(subjects))

# Create bar plots for each student
plt.bar(index, marks_student1, width=bar_width, label='Student 1')
plt.bar(index + bar_width, marks_student2, width=bar_width, label='Student 2')
plt.xticks(index + bar_width / 2, subjects)
plt.ylabel('marks')
plt.legend()

# Show the plot
plt.show()
