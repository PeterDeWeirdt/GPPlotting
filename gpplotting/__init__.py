import seaborn as sns

def example_plot():
    df = sns.load_dataset("iris")
    sns.pairplot(df, hue="species")
