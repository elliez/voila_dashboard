import pandas as pd
import numpy as np
import matplotlib as plt
import seaborn as sns


def radar(df, ax=None):
    # calculate evenly-spaced axis angles
    num_vars = len(df.columns)
    theta = 2 * np.pi * np.linspace(0, 1 - 1.0 / num_vars, num_vars)
    # rotate theta such that the first axis is at the top
    theta += np.pi / 2
    if not ax:
        fig = plt.figure(figsize=(4, 4))

        ax = fig.add_subplot(1, 1, 1, projection="polar")
    else:
        ax.clear()
    for d, color in zip(df.itertuples(), sns.color_palette()):
        ax.plot(theta, d[1:], color=color, alpha=0.7)
        ax.fill(theta, d[1:], facecolor=color, alpha=0.5)
    ax.set_xticklabels(df.columns)

    legend = ax.legend(df.index, loc=(0.9, 0.95))
    return ax


def get_similar(scotch_df_normed, name, n, top=True):
    a = scotch_df_normed[name].sort_values(ascending=False)
    a.name = "Similarity"
    df = pd.DataFrame(a)  # .join(scotch_df).iloc[start:end]
    return df.head(n) if top else df.tail(n)
