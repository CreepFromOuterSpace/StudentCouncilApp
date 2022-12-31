import streamlit as st

username = st.text_input('Email (Use Your ***********@bishopbrady.edu Email)')
password = st.text_input('Password', type="password")

user_list = ["test@user.go"]
pass_list = ["password"]


if st.button('Register'):
  with st.spinner(text="Registering user..."):
    if (username in user_list):
      st.warning('''There's already an account with that email.''')
    else:
      user_list.insert(1, username)
      pass_list.insert(1, password)
      st.success('''Account Registered!''')
