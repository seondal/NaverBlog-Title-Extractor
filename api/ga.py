import requests
from dotenv import load_dotenv
import os

load_dotenv()

GA_ID = os.getenv("GA_ID")
GA_KEY = os.getenv("GA_KEY")

def ga_event(client_id, searched):
    measurement_id = "YOUR_GA4_MEASUREMENT_ID"
    api_secret = "YOUR_API_SECRET"

    url = f"https://www.google-analytics.com/mp/collect?measurement_id={GA_ID}&api_secret={GA_KEY}"
    
    payload = {
        "client_id" : client_id,
        "events": [
            {
                "name": "search",
                "params": {
                    "search_term": searched
                }
            }
        ]
    }

    response = requests.post(url, json=payload)

    # print(payload)
    # print("Sending request to GA4:", json.dumps(payload, indent=2))
    print("Response from GA4:", response.text)

    return response