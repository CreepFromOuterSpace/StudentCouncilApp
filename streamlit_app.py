import streamlit as st

username = st.text_input('Email (Use Your ***********@bishopbrady.edu Email)')
password = st.text_input('Password', type="password")

if st.button('Register'):
  with st.spinner(text="Registering user..."):
    with open(r'users.txt', 'r') as fp:
    lines = fp.readlines()
    for row in lines:
        word = password
        if row.find(word) != -1:
            print('User already exists.')
            print('line Number:', lines.index(line))
