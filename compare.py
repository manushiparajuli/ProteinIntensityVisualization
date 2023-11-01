import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Read data from the Experiment.tsv file
data = pd.read_csv('Experiment.tsv', sep='\t')

# Calculate the log2 values for 'control_1 Intensity_2' and 'control_1 Intensity_1/control_1 Intensity_2'
data['log2(control_1 Intensity_2)'] = np.log2(data['control_1 Intensity_2'])
data['log2(control_1 Intensity_1/control_1 Intensity_2)'] = np.log2(data['control_1 Intensity_1'] / data['control_1 Intensity_2'])

# Read data from the Experiment1.tsv file
data1 = pd.read_csv('Experiment1.tsv', sep='\t')

# Calculate the log2 values for 'control_1 Intensity_2' and 'control_1 Intensity_1/control_1 Intensity_2'
data1['log2(control_1 Intensity_2)'] = np.log2(data1['control_1 Intensity_2'])
data1['log2(control_1 Intensity_1/control_1 Intensity_2)'] = np.log2(data1['control_1 Intensity_1'] / data1['control_1 Intensity_2'])

# Read data from the Experiment2.tsv file
data2 = pd.read_csv('Experiment2.tsv', sep='\t')

# Calculate the log2 values for 'control_1 Intensity_2' and 'control_1 Intensity_1/control_1 Intensity_2'
data2['log2(control_1 Intensity_2)'] = np.log2(data2['control_1 Intensity_2'])
data2['log2(control_1 Intensity_1/control_1 Intensity_2)'] = np.log2(data2['control_1 Intensity_1'] / data2['control_1 Intensity_2'])

# Create a figure that covers the entire screen
fig = plt.figure(figsize=(20, 20))

plt.ylim(-3, 3)


# Scatterplot for Experiment.tsv (purple)
plt.scatter(data['log2(control_1 Intensity_2)'], data['log2(control_1 Intensity_1/control_1 Intensity_2)'],
            c='green', marker='o', alpha=0.5, label='Homo Sapiens')

# Scatterplot for Experiment1.tsv (green)
plt.scatter(data1['log2(control_1 Intensity_2)'], data1['log2(control_1 Intensity_1/control_1 Intensity_2)'],
            c='orange', marker='o', alpha=0.5, label='S. cerevisiae')

# Scatterplot for Experiment2.tsv (red)
plt.scatter(data2['log2(control_1 Intensity_2)'], data2['log2(control_1 Intensity_1/control_1 Intensity_2)'],
            c='blue', marker='o', alpha=0.5, label='E. coli')

# Add labels and title
plt.xlabel('log2(control_1 Intensity_2)')
plt.ylabel('log2(control_1 Intensity_1/control_1 Intensity_2)')
plt.title('Scatterplot of log2(Control_1 Intensity_2) vs. log2(Control_1 Intensity_1/Control_1 Intensity_2)')

# Add a legend to differentiate between the datasets
plt.legend()
plt.xlim(12, max(data['log2(control_1 Intensity_2)']))


# Show the plot
plt.grid()
plt.show()
