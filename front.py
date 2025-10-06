import streamlit as st
from index import *
from time import sleep
import requests

st.header("Bem vindo ao Banco Piton!")

if "pagina" not in st.session_state:
    st.session_state.pagina = "login"


def a_cadastro():
    st.subheader("Área de Cadastro")

    usuario = st.text_input("Digite o nome")
    senha = st.text_input("Digite a senha", type="password")

    cadastrar = st.button("Cadastrar")

    if cadastrar:
        registrar = requests.post(f"http://localhost:5050/register/{usuario}/{senha}") 
        registrar_json = registrar.json()
        if registrar_json["mensagem"] == "Usuario Já cadastrado!":
            st.error("Usuario Já cadastrado!")
        else:
            st.success("Cadastro realizado com sucesso!")
            sleep(0.5)
            st.session_state.pagina = "login"
            st.rerun()

    logar_button = st.button("Ir para login")

    if logar_button:
        st.session_state.pagina = "login"
        st.rerun()


def a_login():
    st.subheader("Área de Login")

    usuario = st.text_input("Digite o nome")
    senha = st.text_input("Digite a senha", type="password")

    login_button = st.button("Logar")

    cadastro_button = st.button("Se cadastrar")

    if login_button:        
        logar = requests.post(f"http://localhost:5050/login/{usuario}/{senha}") 
        logar_json = logar.json()
        if logar_json["mensagem"] == "ERRO! senha errada!" or logar_json["mensagem"] == "Usuário não localizado":
            st.error(logar_json["mensagem"])
        else:
            st.success("Logado com sucesso!")
            sleep(0.5)
            st.session_state.pagina = "painel" 
            st.rerun()
    if cadastro_button:
        st.session_state.pagina = "cadastrar"
        st.rerun()


def painel_usuario():
    st.subheader("Bem-vindo ao painel!")
    st.write("Aqui você pode ver seus dados, histórico, etc.")

    if st.button("Sair"):
        st.session_state.pagina = "login"
        st.rerun()


if st.session_state.pagina == "login":
    a_login()
elif st.session_state.pagina == "painel":
    painel_usuario()
elif st.session_state.pagina == "cadastrar":
    a_cadastro()

    