import matplotlib.pyplot as plt
import numpy as np

def plot(bfd_natural, bfd_occurences, title, bar_label, plot_path):
    # Plotting
    # X axis size
    x = np.arange(start=1, stop=10)

    width = 0.40

    # Width and Height
    fig = plt.figure(figsize=(50,30))

    # Legend and Multiple Bar Graphs
    ax = plt.subplot(111)
    ax.bar(x-0.2, np.array(bfd_natural).flatten().astype(float).tolist(), width, label="Benford's Law")
    ax.bar(x+0.2, bfd_occurences, width, label=bar_label)
    ax.legend(shadow=True, ncol=2, fontsize=30)

    # Set x axis to every available x value
    plt.xticks(x, fontsize=30)
    plt.yticks(fontsize=30)
    ax.tick_params(axis='both', which='major', pad=15)


    # Labels
    plt.xlabel("Leading Digit", fontsize=40, labelpad=40)
    plt.ylabel("Percentage of Occurence", fontsize=40, labelpad=50)
    plt.title(f"Benford's Law and {title}", fontsize=50, pad=40)

    plt.savefig(f"plots/{plot_path}", bbox_inches="tight", pad_inches=1) 
