import streamlit as st

username = st.text_input('Email (Use Your ***********@bishopbrady.edu Email)')
password = st.text_input('Password', type="password")

if st.button('Register'):
  with st.spinner(text="Registering user..."):
    with open(r'users.txt', 'r') as file:
      content=file.read()
      if username in content:
        st.warn('There is already an account with your username...')
      else:
        st.success('Registered an account with username',username)
