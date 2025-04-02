import pandas as pd
import matplotlib.pyplot as plt

if __name__ == '__main__':
    df = pd.read_csv("bank.csv")
    print('Description:\n', df.describe())

    print('\nInfo:')
    df.info()

    numeric_fields = ['age', 'balance']
    stats = df[numeric_fields].agg(['min', 'max', 'mean', 'std'])
    print('\nStatistics:\n', stats)

    fig, axes = plt.subplots(2, 1, figsize=(10, 10))

    for i, col in enumerate(numeric_fields):
        axes[i].hist(df[col], bins=30, edgecolor='grey')
        axes[i].set_title(f'Histogram: {col}')
        axes[i].set_xlabel(col)
        axes[i].set_ylabel('Amount')

    plt.tight_layout()
    plt.show()

    nominal_fields = ['marital', 'deposit']
    fig, axes = plt.subplots(2, 1, figsize=(10, 10))

    for i, col in enumerate(nominal_fields):
        df[col].value_counts().plot(color='orange', kind='bar', ax=axes[i], edgecolor='grey')
        axes[i].set_title(f'Distribution: {col}')
        axes[i].set_xlabel(col)
        axes[i].set_ylabel('Amount')

    plt.tight_layout()
    plt.show()