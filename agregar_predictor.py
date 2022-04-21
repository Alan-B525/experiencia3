import pandas as pd

#Ruta del archivo
ruta='claves_test.csv'

df = pd.read_csv(ruta)

claves = df.Clave

    
df['Longitud'] = len (claves)

#df.drop('Longitud', inplace=True, axis=1)

df.to_csv('claves_test.csv', index=False)

