import streamlit as st
from langchain.llms import OpenAI

st.title('Interfaz gráfica TFG Elena Abad')

openai_api_key = st.sidebar.text_input('OpenAI API Key', type='password')

def generate_response(input_text):
    llm = OpenAI(temperature=0.7, openai_api_key=openai_api_key)
    st.info(llm(input_text))

with st.form('my_form'):
    text = st.text_area('Introduzca una instrucción:', 'Una persona tiene un salario neto de 2000 euros al mes. Solicita una hipoteca por importe de 400000 euros. La tasa de riesgo hipotecario que prescriben entidades como el Banco de España es de un 30 por ciento del salario mensual.¿Cuánto tiene que pagar al mes?"')
    submitted = st.form_submit_button('Enviar')
    if not openai_api_key.startswith('sk-'):
        st.warning('Por favor, introduzca su clave de OpenAI (OpenAI API Key).', icon='⚠')
    if submitted and openai_api_key.startswith('sk-'):
        generate_response(text)