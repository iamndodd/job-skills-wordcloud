import os
import pandas as pd
import requests
from config import *
from dotenv import load_dotenv


# Parameters of API search
def fetch_api_data(job_to_search, save_csv=False):
    url = "https://api.adzuna.com/v1/api/jobs/gb/search/1"
    load_dotenv()
    app_id = os.getenv("app_id") or st.secrets.get("app_id")
    app_key =  os.getenv("app_key") or st.secrets.get("app_key")

    if not app_id or not app_key:
        raise ValueError("Missing API credentials. Check your .env file.")

    params = {
        "app_id": app_id,
        "app_key": app_key,
        "what": job_to_search,
        "results_per_page": 75,  # adjust as needed
        "content-type": "application/json"
    }

    response = requests.get(url, params=params)
    data = response.json()

    jobs = pd.DataFrame(data["results"])
    jobs = jobs.drop_duplicates(subset = "description", keep="last")

    if save_csv:
        jobs.to_csv(DATA_ADZUNA_DIR/f"ADZUNA_{job_to_search}_raw.csv", index = False)

    return jobs