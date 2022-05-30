import math
import matplotlib.pyplot as plt
import seaborn as sns

colors = sns.color_palette('rocket', 3)


def percent_error_calculation(original: float, new: float):
    return abs((new - original)*100/original)


x = [4, 5, 6, 7, 8, 9, 10]
y1 = [-1.07, -0.47, -0.11, 0.12, 0.28, 0.39, 0.46]

plt.plot(x, y1, 'o-', mfc='w', color=colors[0])
plt.ylabel(r'$Flux_{optimal} - Flux_{actual}$ ($\frac{KgSS}{m^3*h}$)')
plt.xlabel(r'Number of FST (No)')
plt.axhline(0, color='black')
plt.title(r'Optimum Number of FST $(No)$')
plt.show()
