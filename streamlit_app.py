import streamlit as st
import os
import base64

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

st.text("Welcome to our speed dating app! To get started, click the button below.")
st.button("Start Dating").bind("Start Dating", start_dating)

# Suggest matches based on likes and dislikes
st.header("Suggested Matches")

for match in data:
    if match in likes and match not in dislikes:
        st.text(f"Name: {match['name']}")
        st.text(f"Age: {match['age']}")
        st.text(f"Location: {match['location']}")
        st.image(match["image"])

# Sidebar for user input
st.sidebar.header("Your Information")

name = st.sidebar.text_input("Name")
age = st.sidebar.number_input("Age")
location = st.sidebar.text_input("Location")

# Image upload
uploaded_file = st.sidebar.file_uploader("Upload your image", type=["jpg", "png"])
if uploaded_file is not None:
    with open(uploaded_file.name, "rb") as f:
        image_bytes = f.read()
    image_data = base64.b64encode(image_bytes).decode()
    image_src = f'data:image/jpeg;base64,{image_data}'
    st.sidebar.image(image_src, width=100)

preferences = st.sidebar.radio("Preferences", ("None", "Age", "Location"))

if preferences == "Age":
    age_range = st.sidebar.slider("Age Range", min_value=18, max_value=99, value=(18, 99))
else:
    location_pref = st.sidebar.text_input("Location Preference")
