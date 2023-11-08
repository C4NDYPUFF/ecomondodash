import streamlit as st 
from ploting import create_histogram, create_pie_charts
import pandas as pd 
import plotly_express as px

def main_app():
    st.set_page_config(page_title='ECOMONDO DASHBOARD', page_icon=':bar_chart:', layout='wide')
    # Main page layout
    st.title(':bar_chart: ECOMONDO VISITANTES 2022 y 2023')
    st.markdown('##')

    fig_categoria = create_histogram(x='Categoria', y='FechaEvento', axis_x_title='Categoria', axis_y_title='Registros', title='Registros por Categoria')

    st.plotly_chart(fig_categoria, use_container_width=True)

    fig_asistencia = create_histogram(x='Asistencia', y='FechaEvento', axis_x_title='Asitencia', axis_y_title='Registros', title='Asistentes por evento de ECOMONDO 2022 y 2023')
    
    st.plotly_chart(fig_asistencia, use_container_width=True)

    data_to_plot = { 
        'Categoria' : ['Total 2022', 'Visitantes que regresaron 2022-2023', 'No Regresaron en 2023'],
        'Asistentes' : [2718, 32, 2686]
    }

    plot_df = pd.DataFrame(data_to_plot)
    fig= px.bar(plot_df, x='Categoria', y='Asistentes', title='Resumen de Asistentes ECCOMONDO')

    st.plotly_chart(fig, use_container_width=True)

    pie_chart = create_pie_charts('Empresa', 'FechaEvento')

    for pie in pie_chart:
        st.plotly_chart(pie, use_container_width=True)

main_app()