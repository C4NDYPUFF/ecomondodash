import streamlit as st 
from ploting import create_histogram, create_pie_charts, plot_pie_chart
import pandas as pd 
import plotly_express as px

def main_app():
    st.set_page_config(page_title='ECOMONDO DASHBOARD', page_icon=':bar_chart:', layout='wide')
    # Main page layout
    st.title(':bar_chart: ECOMONDO VISITANTES 2022 y 2023')
    st.markdown('##')

    data_total = { 
        'Evento' : ['ECOMONDO 2022', 'ECOMONDO 2023'],
        'Registros' : [1848, 4668]
    }

    plot_total = pd.DataFrame(data_total)
    fig_total = px.bar(plot_total, x='Evento', y='Registros', color='Evento', title='Total Registros para cada Evento')
    st.plotly_chart(fig_total, use_container_width=True)
    fig_categoria = create_histogram(x='Categoria', y='FechaEvento', axis_x_title='Categoria', axis_y_title='Registros', title='Registros por tipo de visitante')
    st.plotly_chart(fig_categoria, use_container_width=True)

    fig_asistencia = create_histogram(x='Asistencia', y='FechaEvento', axis_x_title='Asitencia', axis_y_title='Registros', title='Asistentes por evento de ECOMONDO 2022 y 2023')
    
    st.plotly_chart(fig_asistencia, use_container_width=True)

    data_to_plot = { 
        'Categoria' : ['Asistentes 2022', 'Visitantes que regresaron 2023', 'Nuevos Visitantes en 2023'],
        'Asistentes' : [718, 32, 1241]
    }

    plot_df = pd.DataFrame(data_to_plot)
    fig= px.bar(plot_df, x='Categoria', y='Asistentes', title='Resumen de Asistentes ECOMONDO')

    st.plotly_chart(fig, use_container_width=True)

    pie_chart = create_pie_charts('Empresa', 'FechaEvento')

    for pie in pie_chart:
        st.plotly_chart(pie, use_container_width=True)
    
    fig_medio_2022 = plot_pie_chart('2023')
    st.plotly_chart(fig_medio_2022, use_container_width=True)

main_app()