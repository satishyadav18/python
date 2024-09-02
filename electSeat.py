import matplotlib.pyplot as plt
import random

party = ['X', 'Y', 'Z']
seats = []
for i in range(3):
    seats.append(random.randint(200, 700))

plt.bar(party, seats, color=['red','blue', 'yellow'])

plt.xlabel('            party--->')
plt.ylabel('seats--->')
plt.title('election result')
plt.show()