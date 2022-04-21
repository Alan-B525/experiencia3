import pandas as pd
import numpy as np

#Ruta del archivo
ruta='claves.csv'

df = pd.read_csv(ruta)
df['split'] = np.random.randn(df.shape[0], 1)

msk = np.random.rand(len(df)) <= 0.9

train = df[msk]
test = df[~msk]

train.drop('split', inplace=True, axis=1) 
test.drop('split', inplace=True, axis=1) 

train.to_csv('claves_train.csv', index=False)
test.to_csv('claves_test.csv', index=False)
