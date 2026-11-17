import streamlit as st
from consumidor_api import obter_dados

st.set_page_config(
    page_title="Estação Meteorológica",
    page_icon="🌡️",
    layout="centered"
)

st.title("🌡️ Estação Meteorológica")
st.write("Monitoramento das condições ambientais")
st.caption("Jaraguá do Sul — Santa Catarina")

st.divider()

try:
    with st.spinner("Obtendo informações meteorológicas..."):
        dados = obter_dados()

    st.success("Consulta realizada com sucesso!")

    st.subheader("🌡️ Temperatura")

    col1, col2 = st.columns(2)

    col1.metric(
        "A temperatura é:",
        f"{dados["current"]['temperature_2m']:.1f} °C"
    )

    col2.metric(
        "A sensação térmica é:",
        f"{dados["current"]['apparent_temperature']:.1f} °C"
    )

    st.divider()

    st.subheader("💧 Umidade e precipitação")

    st.metric(
        "A umidade é:",
        f"{dados["current"]['relative_humidity_2m']:.0f} %"
    )

    st.metric(
        "A precipitação de chuva é:",
        f"{dados["current"]['precipitation']:.1f} mm"
    )

    st.divider()

    st.subheader("💨 Vento")

    st.metric(
        "O vento está a:",
        f"{dados["current"]['wind_speed_10m']:.1f} km/h"
    )

    st.divider()

    st.info(f"Data/Hora: {dados["current"]['time']}")

except Exception as erro:
    st.error(f"Falha ao obter os dados meteorológicos: {erro}")
