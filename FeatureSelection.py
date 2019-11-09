import pandas as pd 
df = pd.read_csv('aapl.csv')
df_X = df[['High', 'Low', 'Close', 'Volume', 'Adj Close']]

from sklearn.decomposition import PCA
pca = PCA(n_components=5)
pca.fit(df_X)
X_reduced = pca.transform(df_X)
