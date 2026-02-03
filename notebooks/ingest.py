# scorecard_ingest.py

import os
import requests
from dotenv import load_dotenv
import pandas as pd

pd.set_option("display.max_columns", None)

load_dotenv()

SCORECARD_KEY = os.getenv("COLLEGE_SCORECARD_API_KEY")

BASE_URL = "https://api.data.gov/ed/collegescorecard/v1/schools"

fields = ",".join([
    "school.name",
    "latest.aid.loan_principal",
    "latest.earnings.10_yrs_after_entry.working_not_enrolled.mean_earnings"
])

params= {
    "api_key":SCORECARD_KEY,
    "school.state":"FL",
    "fields": fields
}
response = requests.get(
    BASE_URL,
    params = params,
)
data = response.json()

df = pd.json_normalize(data["results"])
print(df.head(10))


