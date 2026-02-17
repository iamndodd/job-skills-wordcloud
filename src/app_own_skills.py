import streamlit as st
from build_wordcloud_style import make_wordcloud_figure_dict
from my_skills import *

# Make app full-width
st.set_page_config(layout="centered")

st.title("My Skills Wordcloud", text_alignment="center")
#st.text("Using python dictionaries to create a wordcloud")

lower = 1
upper = 5

# sidebar
st.sidebar.subheader("Score Your Skills")

Technical_score = st.sidebar.slider("Technical Skills",lower,upper)
Analytical_score = st.sidebar.slider("Analytical Skills",lower,upper)
Communication_score = st.sidebar.slider("Communication Skills",lower,upper)
Collaboration_score = st.sidebar.slider("Collaboration Skills",lower,upper)
Leadership_score = st.sidebar.slider("Leadership Skills",lower,upper)
Organise_score = st.sidebar.slider("Organisational Skills",lower,upper)
Problem_Solving_score = st.sidebar.slider("Problem-Solving Skills",lower,upper)
Adaptability_score = st.sidebar.slider("Adaptability Skills",lower,upper)
Professionalism_score = st.sidebar.slider("Professionalism Skills",lower,upper)
Business_score = st.sidebar.slider("Strategic & Business Skills",lower,upper)
Joke_score = 10


skill_categories = {
    "Being me": 10,
    "Technical Skills": Technical_score,
    "Analytical Skills": Analytical_score,
    "Communication Skills": Communication_score,
    "Collaboration Skills": Collaboration_score,
    "Leadership Skills": Leadership_score,
    "Organizational Skills": Organise_score,
    "Problem-Solving Skills": Problem_Solving_score,
    "Adaptability Skills": Adaptability_score,
    "Professionalism Skills": Professionalism_score,
    "Strategic & Business Skills": Business_score,
    "Joke Skills": Joke_score
}

st.sidebar.text("Alternate Reality?")
if st.sidebar.checkbox("Bad Skills") == True:
    final_cats_score = skill_categories
    final_dict = skills_dict
    message_text = "*** Joke Version ***"
    color = "spring"
else:
    final_cats_score = {cat: score for cat, score in skill_categories.items() if not cat == "Joke Skills"}
    final_dict = {cat: skill_list for cat, skill_list in skills_dict.items() if not cat == "Joke Skills"}
    message_text = "Standard Version"
    color = "gist_yarg"

st.text(message_text, width="stretch", text_alignment= "center")
# Flatten the skills_dict with category scores
weighted_skills_dict = {
    skill: final_cats_score[category]*20+np.random.randint(-12,41)  # score comes from parent category
    for category, subskills in final_dict.items()
    for skill in subskills
}

wordcloud = make_wordcloud_figure_dict(weighted_skills_dict, 125, color= color)

# Create matplotlib figure
fig, ax = plt.subplots(figsize=(8, 8))
# plt.title("My Skills".title())
ax.imshow(wordcloud, interpolation="bilinear")
ax.axis("off")

st.pyplot(fig)


st.text("App Created By Dr. Nathan Dodd 2026", width="stretch", text_alignment= "center")