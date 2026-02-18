import streamlit as st
from build_wordcloud_style import *
from fetch_data_from_api import *
import re

# Make app full-width
st.set_page_config(layout="centered")

# Page titles and text
st.title(":blue[ADZUNA API WORDCLOUD MAKER]", text_alignment= "center")
st.text("This project analyses UK job descriptions using the free Adzuna API. It extracts job descriptions, processes text data, and generates a word cloud to visualize in-demand skills in the current job market.",
        text_alignment= "justify")
st.text("This project intentionally combined independent development with AI-assisted troubleshooting and architectural guidance. While AI supported problem-solving and efficiency, the core codebase was written manually as a hands-on learning exercise. The objective was to demonstrate practical capability in consuming API data, processing and transforming it, and delivering meaningful analytical outputs.",
        text_alignment= "justify")

# Area of page to enter input and make wordcloud
search_term = st.text_input(":blue[_Enter a Job Title or a Skill Here:_]", "Data Science")

# error message at point of search term entry
jobs = fetch_api_data(search_term)
results_length = (len(jobs))

# error message for low and no results
if results_length < 2:
    st.error(f"No job results found for '{search_term}'.")
    st.info("Try a broader keyword or different spelling.")
    st.stop()

# Use search term to get data
# jobs = fetch_api_data(search_term)

# Extract job descriptions
job_descriptions = jobs["description"].tolist()
# Combine into a single string
all_text = " ".join(job_descriptions)
# Basic cleanup: lowercase, remove punctuation
clean_text = re.sub(r"[^a-zA-Z\s]", "", all_text.title())

if clean_text == False or clean_text == "":
    clean_text = "NOT ABLE TO CREATE A WORDCLOUD BUT HERE IS A RANDOM SELECTION OF WORDS"

wordcloud = make_wordcloud_figure(clean_text, 150)

# Create matplotlib figure
fig, ax = plt.subplots(figsize=(10, 5))
plt.title(search_term.title())
ax.imshow(wordcloud, interpolation="bilinear")
ax.axis("off")
st.pyplot(fig)

# page tail
st.text(f"This search returned {results_length} results from the ADZUNA API.", width="stretch", text_alignment= "center")
st.text("App Created By Dr. Nathan Dodd 2026", width="stretch", text_alignment= "center")