from flask import render_template
from flask import current_app as app
import pandas as pd
from .utils import *

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/tenis')
def mostrar_datos():
    # Ejemplo de DataFrames

    # Convertir los DataFrames a HTML
    tabla_df1 = df_bwin.to_html(classes='table-sm table-responsive table-dark table-striped', header="true", index=False, render_links=True)
    tabla_df2 = df_winamax.to_html(classes='table-sm table-responsive table-dark table-striped', header="true", index=False, render_links=True)
    tabla_df3 = df_888.to_html(classes='table-sm table-responsive table-dark table-striped', header="true", index=False, render_links=True)
    tabla_df4 = df_grouped.to_html(classes='table-sm table-responsive table-dark table-striped', header="true", index=False, render_links=True)
    tabla_surebets = pd.DataFrame(calculate_surebet(df_grouped)).to_html(classes='table-sm table-responsive table-dark table-striped', header="true", index=False, render_links=True)
    # Pasar las tablas al template
    return render_template('tabla_datos.html',tabla_df1=tabla_df1,tabla_df2=tabla_df2,tabla_df3=tabla_df3,tabla_df4=tabla_df4,tabla_surebets=tabla_surebets)