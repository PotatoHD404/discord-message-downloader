from dateutil.parser import parse
from datetime import timedelta

from utils import save_json, read_json


def calculate_call_stats():
    all_messages = read_json('all_messages.json')
    call_messages = [msg for msg in all_messages if 'call' in msg]

    num_calls = len(call_messages)
    total_call_length = timedelta()
    call_info = []

    for call in call_messages:
        start_time = parse(call['timestamp'])
        end_time = parse(call['call']['ended_timestamp'])
        call_length = end_time - start_time
        total_call_length += call_length

        call_info.append({
            'start_time': start_time.isoformat(),
            'end_time': end_time.isoformat(),
            'call_length': str(call_length),
            'caller': call['author']['username'],
        })

    save_json('call_info.json', call_info)
    save_json('call_stats.json', {
        'num_calls': num_calls,
        'total_call_length': str(total_call_length),
    })


def main():
    calculate_call_stats()


if __name__ == '__main__':
    main()
