import os
import time
import json
import requests
from dotenv import load_dotenv
from requests.exceptions import RequestException

load_dotenv()

DISCORD_TOKEN = os.getenv('DISCORD_TOKEN')
CHANNEL_ID = os.getenv('CHANNEL_ID')
BASE_URL = f"https://discord.com/api/v9/channels/{CHANNEL_ID}/messages"

headers = {
    'X-Discord-Timezone': 'Europe/Moscow',
    'Authorization': DISCORD_TOKEN,
}


def get_messages(before_id=None):
    params = {'limit': 100}
    if before_id:
        params['before'] = before_id

    for _ in range(3):  # Retry up to 3 times
        try:
            response = requests.get(BASE_URL, headers=headers, params=params)
            response.raise_for_status()
            return response.json()
        except RequestException as e:
            print(f"Request failed with {e}, retrying...")
            time.sleep(1)
    return None


def save_json(filename, data):
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)


def read_json(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        return json.load(f)


def fetch_all_messages():
    before_id = None
    file_counter = 1
    while True:
        messages = get_messages(before_id)
        if not messages:
            print("No more messages or request failed after retries.")
            break
        before_id = messages[-1]['id']  # Get the ID of the last message for the next iteration
        save_json(f'messages_{file_counter}.json', messages)
        file_counter += 1
        time.sleep(1)  # To prevent rate limiting


def main():
    fetch_all_messages()


if __name__ == '__main__':
    main()
