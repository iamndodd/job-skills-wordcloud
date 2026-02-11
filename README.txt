# UK Data Science Skills Analysis using Adzuna API

This project analyzes UK data science job descriptions using the Adzuna API.
It extracts job descriptions, processes text data, and generates a word cloud
to visualize in-demand skills in the current job market.

API credentials are not included for security reasons.
To reproduce the data collection step:
1. Sign up for an Adzuna API key
2. Set environment variables:
   - app_id
   - app_key
3. Run `fetch_jobs.py`

A snapshot of the collected data is provided in `data/raw/`
to allow the analysis to run without API access.

## Motivation

As an aspiring data scientist, I wanted to compare my current skill set
against real job market demand using live API data. This project demonstrates
how APIs, data cleaning, and visualization can be combined into a reproducible
analysis pipeline.

## Project Structure

skills_wordcloud/
│
├── src/
│   ├── main_api_wordcloud.py #builds wordcloud based on job title search
│   ├── main_cv_wordcloud.py #buils wordcloud based on skills dictionary
│   ├── fetch_data_from_api.py #get data using API
│   ├── build_wordcloud_style.py #define wordcloud style
│   └── config.py
│
├── data/
│   ├── ADZUNA_data #collection of API results as CSV
│   └── my_skills.py #dictionary of various data skills
│
├── figures/
│   └── *.png #saved wordcloud images
│
├── requirements.txt
└── README.md


## Methodology

1. Fetch job data using the Adzuna API
2. Save raw results locally
3. Clean and deduplicate job descriptions
4. Combine text into a corpus
5. Generate a weighted word cloud

## Output

![Word Cloud](figures/skills_wordcloud.png)

## Installation

1. Clone the repository
2. Create a virtual environment
3. Install dependencies:

pip install -r requirements.txt

4. Create a .env file with:

app_id=your_id
app_key=your_key

5. Run:

python src/main.py

## Skills Demonstrated

- Python
- REST API integration
- JSON handling
- Environment variable management
- Pandas data processing
- Text cleaning
- Data visualization
- Reproducible project structure
- Secure credential handling

## Future Improvements

- Compare multiple job roles
- Track trends over time
- Deploy interactive dashboard (Streamlit)
- Add NLP-based keyword extraction
