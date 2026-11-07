# This creates the main landing page for the Streamlit application.
# Contains an introduction to the project and guide users to other pages.

import streamlit as st

# PAGE CONFIGURATION
st.set_page_config(
    page_title = "Frog Data Dashboard",
    page_icon = "🐸",
)

# WELCOME PAGE TITLE
st.title("🐸 Frog Data Collection Lab 02")

# COURSE INFORMATION
st.header("CS 1301")

st.subheader("Web Development - Section D")

st.subheader("Raghavi")

# INTRODUCTORY TEXT
st.write("""
Welcome to my Frog Data Collection app! You can navigate between
the pages using the sidebar to the left.

The following pages are available:

1. **Visuals:** Explore graphs comparing different frog species
and their example lengths. You can also select which frogs
you wish to compare!

2. **Survey:** Enter a frog species and its corresponding length
in centimeters. Your data will be saved and displayed on the
Visuals page!
""")