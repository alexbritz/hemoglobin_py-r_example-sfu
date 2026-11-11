# Haemoglobin by age: a small example for the Git demo
# Fictional data. Run with: python haemoglobin_plot.py

# Load the packages we need: numpy for numbers, matplotlib for plots
import numpy as np
import matplotlib.pyplot as plt

# Create the data: one value per patient, in the same order in every list
age         = np.array([34, 47, 52, 61, 70, 28, 45, 66])        # in years
sex         = np.array(["female", "male", "female", "male", "female", "male", "diverse", "female"])
haemoglobin = np.array([13.2, 14.1, 12.8, 13.5, 11.9, 14.6, 13.9, 12.4])   # in g/dL

# Draw a scatter plot: one dot per patient
plt.scatter(age, haemoglobin)
plt.xlabel("Age (years)")           # label of the x-axis
plt.ylabel("Haemoglobin (g/dL)")    # label of the y-axis
plt.title("Haemoglobin by age")     # title of the plot
plt.show()                          # show the plot
