import seaborn as sns
import matplotlib.pyplot as plt


def plot_hist(df, column="Count", bins=6, title="Histogram"):
    sns.histplot(df[column], bins=bins)
    plt.title(title)
    plt.show()


def plot_bar(df, group_col="Area", value_col="Count", agg="mean", title=None):
    grouped = df.groupby(group_col)[value_col].agg(agg).reset_index()
    sns.barplot(data=grouped, x=group_col, y=value_col)
    plt.xticks(rotation=30)
    plt.title(title or f"{agg.title()} {value_col} by {group_col}")
    plt.show()
