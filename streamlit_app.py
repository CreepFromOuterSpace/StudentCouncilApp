import streamlit as st
import sqlite3

# Connect to the database
conn = sqlite3.connect("users.db")
cursor = conn.cursor()

# Create the "users" table if it doesn't already exist
cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    email TEXT NOT NULL,
    password TEXT NOT NULL
)
""")
conn.commit()

def register(email, password):
    cursor.execute("INSERT INTO users (email, password) VALUES (?, ?)", (email, password))
    conn.commit()

def login(email, password):
    cursor.execute("SELECT * FROM users WHERE email=? AND password=?", (email, password))
    user = cursor.fetchone()
    return user is not None

# Main app layout
st.title("Speed Dating App")

# Sidebar for login and registration
st.sidebar.header("Login")

email = st.sidebar.text_input("Email")
password = st.sidebar.password_input("Password")

if st.sidebar.button("Login"):
    if login(email, password):
        # Redirect to main speed dating page
        st.success("Login successful!")
    else:
        st.error("Invalid email or password")

st.sidebar.header("Registration")

email = st.sidebar.text_input("Email")
password = st.sidebar.password_input("Password")
confirm_password = st.sidebar.password_input("Confirm Password")

if st.sidebar.button("Register"):
    # Validate input
    if not email:
        st.error("Email is required")
    elif not password:
        st.error("Password is required")
    elif password != confirm_password:
        st.error("Passwords do not match")
    else:
        # Check if email is already in use
        cursor.execute("SELECT * FROM users WHERE email=?", (email,))
        user = cursor.fetchone()
        if user:
            st.error("Email is already in use")
        else:
            # Add user to the database
            register(email, password)
            st.success("Registration successful!")

# Main speed dating page
if login(email, password):
    pass
else:
    st.warning("Please log in or register to use the app.")
