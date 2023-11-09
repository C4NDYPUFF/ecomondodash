import streamlit as st 
import plotly_express as px 
from data_processing import load_data

df = load_data(st.secrets['CSV_FILE_PATH'], st.secrets['EXCEL_FILE_PATH'])




###CATEGORIAS POR EVENTO ### 
df_filtered = df[df['Asistencia']=='SI']
df_filtered = df.dropna(subset=['Categoria', 'FechaEvento'])
categoria_list = ['EXPOSITOR ECOMONDO', 'ESTUDIANTE ECOMONDO', 'VISITANTE ECOMONDO']
df_filtered = df_filtered[df_filtered['Categoria'].isin(categoria_list)]

def create_histogram(x, y, axis_x_title, axis_y_title, title):

    fig = px.histogram(df_filtered, x=x, color=y)

    fig.update_layout(
        xaxis_title= axis_x_title,
        yaxis_title= axis_y_title,
        title=title,
        xaxis={'categoryorder':'total descending'},
        bargap=0.2,

    )

    return fig 

def create_pie_charts(name1, name2):
    # Filter the DataFrame for 'Asistencia' == 'SI'
    df_yes = df[df['Asistencia'] == 'SI']
    # Group the data by 'Empresa', 'Asistencia', and 'FechaEvento', then count the occurrences
    table = df_yes.groupby([name1, name2]).size().reset_index(name='Cantidad')
    # Get unique dates
    unique_dates = table['FechaEvento'].unique()
    # Create a list to hold the figures
    figs = []
    # Create a pie chart for each unique date
    for date in unique_dates:
        df_filtered = table[table['FechaEvento'] == date]
        df_filtered = df_filtered.copy()
        map_NAN = {'NAN' : 'OTROS'}
        df_filtered['Empresa'] = df_filtered['Empresa'].replace(map_NAN)
        fig = px.pie(df_filtered, values='Cantidad', names='Empresa', title=f'Distribucion por Categoria {date}')
        figs.append(fig)
    
    return figs