# This creates the page for displaying data visualizations.

import streamlit as st
import pandas as pd
import os
import json
import matplotlib.pyplot as plt

# PAGE CONFIGURATION
st.set_page_config(
    page_title="Visuals",
    page_icon="📈",
)

# PAGE TITLE
st.title("Data Visualizations 📈")


# PART 1: GRAPHS FROM data.json

import streamlit as st
import json
import matplotlib.pyplot as plt
with open("data.json", "r") as file:
    data = json.load(file)
names = []
lengths = []

for frog in data["data_points"]:
    names.append(frog["label"])
    lengths.append(frog["value"])
plt.bar(names, lengths)

plt.title("Comparing Frog Species")
plt.xlabel("Frog Species")
plt.ylabel("Example Length (cm)")
plt.xticks(rotation=30, ha="right")
plt.tight_layout()

# Show the graph
st.pyplot(plt.gcf())
plt.close()


# SECOND GRAPH: Choose which frogs to compare


st.header("Compare Frog Species")

# Remember the selected frog
if "chosen_frogs" not in st.session_state:
    st.session_state.chosen_frogs = names[:2]

# Let the user choose frogs
chosen_frogs = st.multiselect(
    "Choose frogs to compare:",
    names,
    default=st.session_state.chosen_frogs
)

# Save the user's choices
st.session_state.chosen_frogs = chosen_frogs

# Make a scatter plot
chosen_names = []
chosen_lengths = []

for frog in data["data_points"]:
    if frog["label"] in chosen_frogs:
        chosen_names.append(frog["label"])
        chosen_lengths.append(frog["value"])

fig, ax = plt.subplots()
ax.scatter(chosen_names, chosen_lengths)

ax.set_title("Comparing Frog Species")
ax.set_xlabel("Frog Species")
ax.set_ylabel("Example Length (cm)")

plt.xticks(rotation=30, ha="right")
plt.tight_layout()

st.pyplot(fig)
plt.close(fig)
#part 2
st.header("Frog Survey Results")
if os.path.exists("data.csv") and os.path.getsize("data.csv") > 0:
    survey_data = pd.read_csv("data.csv")
    st.dataframe(survey_data)
    frog_options = survey_data["Category"].unique().tolist()
    chosen_frogs = st.multiselect(
        "Select the frogs you want to compare:",
        frog_options,
        default = frog_options,
        key = "survey_frog_selection"
    )
    filtered_data = survey_data[
    survey_data["Category"].isin(chosen_frogs)
    ]
    fig2, ax2 = plt.subplots()
    ax2.bar(filtered_data["Category"], filtered_data["Value"])
    ax2.set_title("Selected Frog Species")
    ax2.set_xlabel("Frog Species")
    ax2.set_ylabel("Example Length (cm)")
    plt.xticks(rotation=30, ha="right")
    plt.tight_layout()
    st.pyplot(fig2)
    plt.close(fig2)
    fig, ax = plt.subplots()
    ax.bar(survey_data["Category"], survey_data["Value"])
    ax.set_title("Frog Survey Results")
    ax.set_xlabel("Frog Species")
    ax.set_ylabel("Example Length (cm)")
    plt.xticks(rotation=30, ha="right")
    plt.tight_layout()
    st.pyplot(fig)
    plt.close(fig)

else:
    st.warning("No survey data has been collected yet.")