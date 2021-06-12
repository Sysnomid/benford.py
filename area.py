import pandas as pd
import math
from plot import plot 

df = pd.read_csv("data/country-population.csv", usecols=['Land Area (Km²)'])

bfd_data = []
bfd_occurences = []
bfd_natural = []

for index, row in df.iterrows():
    # Fetch data from 'Land Area' column in CSV column, and cast it to an int type
    pop_data = df['Land Area (Km²)'][index].astype(int)
   
    # Leading digit finder
    data = str(pop_data)[:1].split()
    bfd_data.append(data)


for i in range(1, 10):
    # Get the amount of occurences of numbers 1 through 9 in the data, and turn it into a percent
    bfd_occurences.append(math.floor((float(bfd_data.count([f'{i}']))/len(bfd_data))*100))
    
    # Benford's law - log10 (i + 1) - log10 (i)
    bfd_log = (math.log10(i + 1) - math.log10(i)) * 100 
    bfd_natural.append(str(round(bfd_log, 2)).split())

plot(bfd_natural, bfd_occurences, "2020 World Land Area", "Land Area", "area.png")
