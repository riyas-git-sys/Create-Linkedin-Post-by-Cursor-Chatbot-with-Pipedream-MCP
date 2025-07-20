import time
import requests

def post_to_linkedin(text, image_url, max_retries=3):
    retry_delay = 60  # Seconds
    for attempt in range(max_retries):
        response = requests.post(
            "YOUR_MCP_SERVER_ENDPOINT",
            json={"text": text, "image_url": image_url}
        )
        if response.status_code == 429:
            print(f"Rate limited. Retry in {retry_delay} secs...")
            time.sleep(retry_delay)
            retry_delay *= 2  # Exponential backoff
        else:
            return response
    raise Exception("Max retries exceeded.")