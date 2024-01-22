#import des librairies pandas et numpy
import numpy as np
import pandas as pd
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
#importation du dataframe extrait de DHIIS2
df= pd.read_excel("/home/romuald-ndzana/Documents/Extrait DHIS2/01_Nov _Dec_2023.xls", sheet_name="Sheet 1")
ent=df.iloc[0]#creation de la variable ent qui est une liste qui va être inséré en entête
df.drop(index=0, inplace=True) #étant donné que cette ligne est promue en entête il est important de la supprimer
df.columns=ent
col_titles=df.columns.to_list()#creation de la liste des titres de collunnes
print(col_titles)
