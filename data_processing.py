import pandas as pd 
import streamlit as st 


def load_data(file_path_csv, file_path_excel):
    data2022 = pd.read_csv(file_path_csv)
    data2023 = pd.read_excel(file_path_excel)

    data2023.rename(columns= {'Cargo / AreaEstudio' : 'Cargo'}, inplace=True)

    data2022['FechaEvento'] = '2022'
    data2023['FechaEvento'] = '2023'

    df = pd.concat([data2022, data2023])

    maping_dict = {True : 'SI', False : 'NO'}
    df['Asistencia'] = df['Asistencia'].replace(maping_dict)

    categoria_map = {'EXPOSITOR ECO': 'EXPOSITOR ECOMONDO', 'ESTUDIANTE ECO': 'ESTUDIANTE ECOMONDO', 'VISITANTE ECO': 'VISITANTE ECOMONDO'}
    df['Categoria'] = df['Categoria'].replace(categoria_map)

    # Convert 'Empresa' column to uppercase strings, NaN values will become 'nan' after this operation
    df['Empresa'] = df['Empresa'].astype(str).str.upper()
    # Define the string you want to match
    match_string = 'UNIVERSIDAD'
    # Use apply() to iterate over the 'Empresa' column and apply the condition
    df['Empresa'] = df['Empresa'].apply(lambda x: 'UNIVERSIDAD' if match_string in x else ('NAN' if x == 'NAN' else 'EMPRESA'))

    return df



def map_medio(medio):
    if pd.isna(medio):
        return 'INFORMACION NO DISPONIBLE'
    medio_str = str(medio).upper()
    redes = ['FACEBOOK', 'INSTAGRAM', 'LINKEDIN', 'TWITTER', 'TIKTOK']
    for name in redes:
        if medio_str == name:
            return 'REDES SOCIALES'
    if medio_str == 'INVITADO POR EXPOSITOR':
        return 'INVITADO POR EXPOSITOR'
    else:
        return medio_str