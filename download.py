import os
import time
import requests
from dotenv import load_dotenv
from requests.exceptions import RequestException

from utils import read_json, save_json

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


def fetch_all_messages():
    before_id = None
    file_counter = 1
    # Create a directory for messages if it doesn't exist
    if not os.path.exists('messages'):
        os.makedirs('messages')

    # if there are already messages saved, get the ID of the last message
    if os.path.exists('messages'):
        files = os.listdir('messages')
        if files:
            messages = read_json(f'messages/{files[-1]}')
            before_id = messages[-1]['id']
            file_counter = int(files[-1].split('_')[-1].split('.')[0]) + 1

    while True:
        messages = get_messages(before_id)
        if not messages:
            print("No more messages or request failed after retries.")
            break
        before_id = messages[-1]['id']  # Get the ID of the last message for the next iteration
        save_json(f'messages/{file_counter}.json', messages)
        file_counter += 1
        time.sleep(10 * 60 / 9000)  # To prevent rate limiting 10,000 per 10 minutes


def main():
    fetch_all_messages()


if __name__ == '__main__':
    main()
