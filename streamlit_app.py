import streamlit as st

username = st.text_input('Username')
password = st.text_input('Password', type="password")
st.button('Register')
