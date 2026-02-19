import streamlit as st
from build_wordcloud_style import make_wordcloud_figure_dict
from my_skills import *

# Make app full-width
st.set_page_config(layout="centered")

st.title(":red"+"[Making a Skills Wordcloud]".upper(), text_alignment="center")

lower = 1
upper = 5

# sidebar
# st.sidebar.subheader("Score Your Skills")
st.text("Create a wordcloud based on the types of skills and personality you have. sliders score skills from 1-5.")
col1, col2, col3, col4, col5 = st.columns(5)
with col1:
    Technical_score = st.slider("Technical",lower,upper)
    Analytical_score = st.slider("Analytical",lower,upper)
with col2:
    Communication_score = st.slider("Communication",lower,upper)
    Collaboration_score = st.slider("Collaboration",lower,upper)
with col3:
    Leadership_score = st.slider("Leadership",lower,upper)
    Organise_score = st.slider("Organisational",lower,upper)
with col4:
    Problem_Solving_score = st.slider("Problem-Solving",lower,upper)
    Adaptability_score = st.slider("Adaptability",lower,upper)
with col5:
    Professionalism_score = st.slider("Professionalism",lower,upper)
    Business_score = st.slider("Strategic & Business",lower,upper)

Joke_score = 10

skill_categories = {
    "Being me": 15,
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

# add terms to joke skills list
new_skill = st.sidebar.text_input("Want to add a terrible talent to the list of bad skills?", "")
new_skill = new_skill.upper()
avoid_terms = "cock,nan,pussy,cunt,fuck,shit,bastard,twat,reece,elliot,elliott,phil,jamie,nathan,dodd,shitty,penis".upper()
if new_skill != "" and new_skill not in joke_skills and new_skill not in avoid_terms:
    if new_skill.isalpha() == True:
        st.sidebar.info("Accepted")
        joke_skills.append(new_skill)
    elif new_skill.isalpha() == False:
        st.sidebar.info("Check Spelling")
elif new_skill == "cunt".upper():
    st.sidebar.error("That is very offensive! I have reported this to the authorities in your local area of [Yorkshire]".upper())
elif new_skill in avoid_terms:
    st.sidebar.error("Rejected!")
else:
    st.sidebar.info("want to add a new (bad) talent?")


st.sidebar.text("Turn on Alternate Reality?")
if st.sidebar.checkbox("Bad Skills") == True:
    final_cats_score = skill_categories
    final_dict = skills_dict
    message_text = "*** Joke Version ***"
    color = "spring"
else:
    final_cats_score = {cat: score for cat, score in skill_categories.items() if not cat == "Joke Skills"}
    final_dict = {cat: skill_list for cat, skill_list in skills_dict.items() if not cat == "Joke Skills"}
    message_text = "Standard Version"
    color = "RdGy_r"

# Flatten the skills_dict with category scores
weighted_skills_dict = {
    skill: final_cats_score[category]*20+np.random.randint(-12,41)  # score comes from parent category
    for category, subskills in final_dict.items()
    for skill in subskills
}

# generate wordcloud
wordcloud = make_wordcloud_figure_dict(weighted_skills_dict, 125, color= color)
st.subheader(f":red[{message_text.upper()}]", width="stretch", text_alignment= "center")
# Create matplotlib figure
fig, ax = plt.subplots(figsize=(8, 8))
# plt.title("My Skills".title())
ax.imshow(wordcloud, interpolation="bilinear")
ax.axis("off")
st.pyplot(fig)

# split main area into 2 columns
colA, colB = st.columns(2)
with colA:
    st.text("""
    This application generates a dynamic word cloud using structured Python dictionaries and a frequency-weighting algorithm. Each word in the visualization is mapped to a score, allowing the cloud to reflect relative importance through size scaling.

    The interface is fully interactive. Sliders allow users to adjust parameters such as word count limits and visual scaling, while checkboxes toggle specific transformation rules and weighting logic. Default parameter states are carefully defined so that each control can be safely turned on and off without breaking the rendering logic or introducing inconsistent states.

    The word cloud shape is defined using a custom PNG mask (a cloud silhouette), which constrains the layout algorithm to render words within the specified figure boundary rather than a default rectangular canvas.
    """, text_alignment="justify")

# wordcloud figure in right col
with colB:
    st.text("""
    This project demonstrates:
    
    - Structuring static data into reusable dictionaries.
    
    - Transforming hierarchical skill data into weighted frequencies.
    
    - Building reactive UI logic in Streamlit.
    
    - Managing stateful controls with predictable defaults.
    
    - Generating custom-shaped word clouds using image masks.
    
    - Connecting user inputs to real-time visual outputs.

    Overall, the app showcases how backend data structures, transformation logic, and frontend controls can be integrated into a cohesive, interactive visualization tool.
    """, width="stretch", text_alignment="left")

st.text("App Created By Dr. Nathan Dodd 2026", width="stretch", text_alignment="center")