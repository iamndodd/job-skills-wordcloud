import matplotlib.pyplot as plt
import pandas as pd
from build_wordcloud_style import make_wordcloud_figure
from config import DATA_ADZUNA_DIR, FIGURE_DIR
from src.fetch_data_from_api import fetch_api_data

# List of job titles to create wordcloud for
job_search_list = ["data scientist",
                   "data analyst",
                   "data analysis",
                   "analyst",
                   "manager",
                   "senior",
                   "junior"]

for job in job_search_list:
    fetch_api_data(job)

# Job search results saved into CSV files
csv_files = list(DATA_ADZUNA_DIR.glob("*.csv"))
print(f"Found {len(csv_files)} CSV files")
print(csv_files)

index = 0
for file in csv_files:
    # Get job title for figure title from fetch_data
    figure_title = job_search_list[index]
    index += 1

    # Read in CSV data to df
    jobs = pd.read_csv(file)

    # Extract job descriptions
    job_descriptions = jobs["description"].tolist()

    # Combine into a single string
    all_text = " ".join(job_descriptions)
    print(all_text[:500])  # preview first 500 characters

    import re
    # Basic cleanup: lowercase, remove punctuation
    clean_text = re.sub(r"[^a-zA-Z\s]", "", all_text.title())

    # Create and save wordcloud image for portfolio use
    wordcloud = make_wordcloud_figure(clean_text, 100)
    plt.title(figure_title.title())
    print(f"saving to {FIGURE_DIR}")
    plt.savefig(FIGURE_DIR/f"adzuna_api_wordcloud_{figure_title}.png", bbox_inches="tight", dpi=1200)
    plt.show()
    print(f"Finished {figure_title.title()}")