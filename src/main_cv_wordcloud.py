from build_wordcloud_style import *
from data.my_skills import skills_text
from config import FIGURE_DIR

# Save for portfolio use
make_wordcloud_figure(skills_text, 200)
plt.title("my skills".title())
plt.savefig(FIGURE_DIR/"my_skills_wordcloud.png", bbox_inches="tight", dpi=1200)
plt.show()