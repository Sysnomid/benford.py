import pandas as pd
import math
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv("country-population.csv", usecols=['Population (2020)'])

bfd_data = []
bfd_occurences = []
bfd_natural = []

for index, row in df.iterrows():
    # Fetch data from 'Population (2020)' column in CSV column, and cast it to an int type
    pop_data = df['Population (2020)'][index].astype(int)
   
    # Leading digit finder
    data = str(pop_data)[:1].split()
    bfd_data.append(data)


for i in range(1, 10):
    # Get the amount of occurences of numbers 1 through 9 in the data, and turn it into a percent
    bfd_occurences.append(math.floor((float(bfd_data.count([f'{i}']))/len(bfd_data))*100))
    
    # Benford's law - log10 (i + 1) - log10 (i)
    bfd_log = (math.log10(i + 1) - math.log10(i)) * 100 
    bfd_natural.append(str(round(bfd_log, 2)).split())

# Plotting
# X axis size
x = np.arange(start=1, stop=10)

width = 0.40

# Width and Height
fig = plt.figure(figsize=(15,10))

# Legend and Multiple Bar Graphs
ax = plt.subplot(111)
ax.bar(x-0.2, np.array(bfd_natural).flatten().astype(float).tolist(), width, label="Benford's Law")
ax.bar(x+0.2, bfd_occurences, width, label='Population')
ax.legend(shadow=True, ncol=2)

# Set x axis to every available x value
plt.xticks(x)

# Labels
plt.xlabel("Leading Digit")
plt.ylabel("Percentage of Occurence")
plt.title("Benford's Law and World Population", fontsize=20)

plt.savefig("benford.png") 
