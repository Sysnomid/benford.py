import pandas as pd
import yfinance as yf
import numpy as np
import math
import matplotlib.pyplot as plt
import datetime

df = pd.read_csv("russell2000.csv", usecols=['Ticker'])

russell_2000_list = []
bfd_data = []
bfd_occurences = []
bfd_natural = []


for index, row in df.iterrows():
    # Fetch data from 'Symbol' column in CSV column, and cast it to an int type
    russell_2000_list.append(df['Ticker'][index])
   
stock_data = yf.download(tickers = " ".join(russell_2000_list), period = "1d")
stock_data_close = stock_data['Close'].to_string(index=False, header=False).replace("\n", " ").split(" ")

for i in range(len(stock_data_close)):
    data = stock_data_close[i]
    sdc = data[:1]
    bfd_data.append(str(sdc))

for i in range(1, 10):
    # Get the amount of occurences of numbers 1 through 9 in the data, and turn it into a percent
    bfd_occurences.append(float(bfd_data.count(f'{i}')/len(bfd_data))*100)
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
ax.bar(x+0.2, bfd_occurences, width, label='Russell 2000 Component Closing Prices')
ax.legend(shadow=True, ncol=2)

# Set x axis to every available x value
plt.xticks(x)

# Labels
plt.xlabel("Leading Digit")
plt.ylabel("Percentage of Occurence")
plt.title(f"Benford's Law and Russell 2000 Component Closing Prices of {datetime.date.today().strftime('%Y-%m-%d')}", fontsize=20)

plt.savefig("benford.png") 
