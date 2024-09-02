import numpy as np
import matplotlib.pyplot as plt
student1_marks = np.random.randint(40, 100, size = 6)
student2_marks = np.random.randint(40, 100, size = 6)
test = np.arange(1,7)
bar_width = .35
plt.bar( test - bar_width/2, student1_marks, bar_width, label = 'student1')
plt.bar( test + bar_width/2, student2_marks, bar_width, label = 'student2')
plt.xlabel('test')
plt.ylabel('marks')
plt.title('marks of 6 unit tests')
plt.legend()

plt.show()