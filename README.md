# Discord Message Downloader

This repository contains Python scripts for fetching, storing, and analyzing
messages from a Discord channel.

## Setup

1. Clone this repository to your local machine.
2. Install the required Python packages using pip:

    ```
    pip install requests python-dotenv
    ```

3. Create a `.env` file in the same directory as your scripts. This file should
contain your Discord token and the ID of the channel you want to fetch messages
from:

    ```
    DISCORD_TOKEN=your_discord_token
    CHANNEL_ID=your_channel_id
    ```

    Replace `your_discord_token` with your actual Discord token, and
`your_channel_id` with the ID of your channel.

## Usage

1. Run `download.py` to fetch all messages from the specified Discord channel
and save them to separate JSON files in the `messages` directory:

    ```
    python fetch_messages.py
    ```

2. Run `combine.py` to merge all the message files into one and sort the
messages by the timestamp:

    ```
    python merge_and_sort_messages.py
    ```

3. Run `filter_calls.py` to filter out the call messages and calculate the call
statistics:

    ```
    python calculate_call_stats.py
    ```

This will create two JSON files: `call_info.json`, which contains information
about each call, and `call_stats.json`, which contains the total number of calls
and the total length of all calls.

## Note

These scripts do not handle rate limits from the Discord API. If you're planning
to fetch a large number of messages, you might need to add some logic to handle
rate limits.
