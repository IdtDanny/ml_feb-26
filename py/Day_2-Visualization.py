import matplotlib.pyplot as plt
import pandas as pd

data = {'TransactionAmount': [50,75,100,45,60,55,1200,80,90,3000,655]}
df = pd.DataFrame(data)

print(f'{df}')

plt.boxplot(df['TransactionAmount'])
plt.title('Transaction Amount BoxPlot')
plt.ylabel('Amount')
plt.show()

# --------------------------------------------------------------------

# Exercise
x = [1,2,3,4,5]
y = [2,3,5,7,11]
plt.plot(x,y, color='red', marker='o', linestyle='--', linewidth=2)
plt.title('Simple Line Plot')
plt.xlabel('Y-axis', fontsize=12)
plt.ylabel('X-axis')
plt.grid(True)
plt.savefig('prime_plot.png')
plt.show()