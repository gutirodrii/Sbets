import pandas as pd
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from scraping.bwin import get_data as bwindata
from scraping.winamax import get_data as winamaxdata
from scraping._888sport import get_data as _888

df_bwin = pd.DataFrame(bwindata())
df_winamax = pd.DataFrame(winamaxdata())
df_888 = pd.DataFrame(_888())

df_combined = pd.concat([df_bwin, df_winamax, df_888], ignore_index=True)

# Agrupar por 'matchId' y obtener el índice de la fila con el máximo 'competitor1Cuote'
# Seleccionar esas filas y renombrar la columna 'url' a 'url1'
idx_max_cuote1 = df_combined.groupby('matchId')['competitor1Cuote'].idxmax()
df_max_cuote1 = df_combined.loc[idx_max_cuote1, ['matchId', 'status', 'competitor1Name','competitor1Cuote', 'url']].rename(columns={'url': 'url1'})

# Agrupar por 'matchId' y obtener el índice de la fila con el máximo 'competitor2Cuote'
# Seleccionar esas filas y renombrar la columna 'url' a 'url2'
idx_max_cuote2 = df_combined.groupby('matchId')['competitor2Cuote'].idxmax()
df_max_cuote2 = df_combined.loc[idx_max_cuote2, ['matchId', 'competitor2Name','competitor2Cuote', 'url']].rename(columns={'url': 'url2'})

# Combinar los DataFrames en base a 'matchId'
df_grouped = pd.merge(df_max_cuote1, df_max_cuote2, on='matchId', how='outer')

# df_grouped = df_combined.groupby(['matchId']).max()

def calculate_surebet(df):
    res = []
    for row in df.itertuples():
        cuote1 = row.competitor1Cuote
        cuote2 = row.competitor2Cuote
        calc = (1/cuote1 + 1/cuote2) if cuote1!=0 and cuote2!=0 else 100
        if calc < 1.01:
            res.append(row)
        else:
            pass
    return res

