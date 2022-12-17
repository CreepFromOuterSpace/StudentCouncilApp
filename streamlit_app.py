import streamlit as st
import os
import base64
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

# Data for potential matches
data = [
    {
        "name": "Alice",
        "age": 26,
        "location": "New York",
        "image": "alice.jpg"
    },
    {
        "name": "Bob",
        "age": 32,
        "location": "Chicago",
        "image": "bob.jpg"
    },
    # Add more potential matches here...
]

# User's likes and dislikes
likes = []
dislikes = []

def start_dating():
    # Display information for each potential match
    for match in data:
        name = match["name"]
        age = match["age"]
        location = match["location"]
        image = match["image"]

        st.text(f"Name: {name}")
        st.text(f"Age: {age}")
        st.text(f"Location: {location}")
        st.image(image)

        # Like or dislike button
        if st.button("Like"):
            likes.append(match)
        elif st.button("Dislike"):
            dislikes.append(match)

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
