import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

def plot_histograms(df, columns):
    cols = 3
    rows = (len(columns) + cols - 1) // cols
    fig, axes = plt.subplots(rows, cols, figsize=(cols * 6, rows * 4))
    axes = axes.flatten()

    for i, col in enumerate(columns):
        sns.histplot(df[col], bins=25, ax=axes[i], color='skyblue', kde=True)
        for line in axes[i].lines:
            line.set_color('red')
        axes[i].set_title(f'Distribution of {col}')
        axes[i].set_xlabel(col)

    for j in range(i + 1, len(axes)):
        fig.delaxes(axes[j])

    plt.tight_layout()
    plt.show()
