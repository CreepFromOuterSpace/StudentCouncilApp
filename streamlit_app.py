import streamlit as st
user_list = ["test@user.go"]
pass_list = ["password"]


col1, col2 = st.columns(2)

with col1:
  username = st.text_input('Email (Use Your ***********@bishopbrady.edu Email)')
  password = st.text_input('Password', type="password")

  if st.button('Register'):
   with st.spinner(text="Registering user..."):
     if (username in user_list):
       st.warning('''There's already an account with that email.''')
     else:
       user_list.insert(0, username)
       pass_list.insert(0, password)
       st.success('''Account Registered!''')
with col2:
  username = st.text_input('Email (Use Your ***********@bishopbrady.edu Email)')
  password = st.text_input('Password', type="password")

  login_user = st.text_imput('Email')
  login_pass = st.text_input('Password', type="password")
  
  if st.button('Login'):
    with st.spinner(text="Logging in..."):
      if (login_user in user_list):
        index = user_list.index(login_user)
        if pass_list[index] == login_pass:
          st.success('Logged in!')
      else:
        st.warning('''I couldn't find an account with that email. Please register first.''')
