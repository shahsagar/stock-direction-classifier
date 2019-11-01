import pandas


def assign_label(filepath):
    df = pandas.read_csv(filepath)
    df['Label'] = (df['Close'] > df['Open']).astype(int)
    print(df.head())


if __name__ == '__main__':
    assign_label('data/aapl.csv')
