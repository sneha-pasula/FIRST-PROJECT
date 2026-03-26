import streamlit as st
import pandas as pd
from datetime import datetime

st.title("🎂 Birthday Reminder")

# Upload CSV
csv_file = st.file_uploader("Upload CSV file", type=["csv"])

if csv_file:
    data = pd.read_csv(csv_file)
    data["Birthday"] = pd.to_datetime(data["Birthday"])
else:
    data = pd.DataFrame(columns=["Name", "Birthday"])

# Upload image
image_file = st.file_uploader("Upload Image", type=["jpg", "jpeg", "png"])

if image_file:
    st.image(image_file, caption="Uploaded Image")

# Manual input
name = st.text_input("Enter Name")
date = st.date_input("Select Birthday")

if st.button("Add"):
    new_row = pd.DataFrame([[name, date]], columns=["Name", "Birthday"])
    data = pd.concat([data, new_row], ignore_index=True)

# Show data
st.write("### All Birthdays")
st.write(data)

# Upcoming birthdays
st.write("### Upcoming Birthdays")

today = datetime.today().date()

for i in range(len(data)):
    bday = pd.to_datetime(data.loc[i, "Birthday"]).date()
    person_name = data.loc[i, "Name"]

    next_bday = bday.replace(year=today.year)

    if next_bday < today:
        next_bday = next_bday.replace(year=today.year + 1)

    days_left = (next_bday - today).days

    if days_left == 0:
        st.success(f"🎉 Today is {person_name}'s Birthday!")
        st.balloons()
    else:
        st.write(f"{person_name} - {days_left} days left 🎂")