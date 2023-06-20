import os
import json
from dateutil.parser import parse

from utils import read_json, save_json


def merge_and_sort_messages():
    all_messages = []
    files = sorted(os.listdir('messages'), key=lambda x: int(x.split('_')[-1].split('.')[0]))

    for file in files:
        messages = read_json(f'messages/{file}')
        all_messages.extend(messages)

    all_messages.sort(key=lambda x: parse(x['timestamp']))
    save_json('all_messages.json', all_messages)


def main():
    merge_and_sort_messages()


if __name__ == '__main__':
    main()
