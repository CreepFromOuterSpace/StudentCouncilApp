import streamlit as st

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

preferences = st.sidebar.radio("Preferences", ("None", "Age", "Location"))

if preferences == "Age":
    age_range = st.sidebar.slider("Age Range", min_value=18, max_value=99, value=(18, 99))
else:
    location_pref = st.sidebar.text_input("Location Preference")

st.sidebar.button("Update Preferences")

# Use preferences to filter and suggest matches
if preferences == "Age":
    suggested_matches = [
        match for match in data
        if match["age"] >= age_range[0] and match["age"] <= age_range[1]
        and match not in likes and match not in dislikes
    ]
elif preferences == "Location":
    suggested_matches = [
        match for match in data
        if location_pref in match["location"]
        and match not in likes and match not in dislikes
    ]
else:
    suggested_matches = []
       
