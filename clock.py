from datetime import datetime
from random import random, choice

import pytz


emoji = '😂🤣👌🔥💯😍'


def format_time(time):
    return datetime.strftime(time, '%H:%M')


def annotate(string):
    original_string = string

    if random() < 9/10:
        string += ' XD{}'.format(('D' * int((random() ** 1.5) * 20)))

    emoji_necessity = 2/3
    string += ' '

    while random() < emoji_necessity:
        emoji_necessity /= 2
        string += (choice(emoji) * int((random() ** 1.5) * 10))

    string = string.strip()

    if original_string == string:
        # no switches were flicked, try again
        return annotate(string)
    else:
        return string


def get_time():
    tz = pytz.timezone('Europe/London')
    now = datetime.now(tz=tz)

    if (now.hour, now.minute) == (13, 37):
        return annotate(format_time(now))
    elif random() < (1/240):
        return format_time(now)
    else:
        return None


if __name__ == '__main__':
    time = get_time()
    if time is not None:
        print(time)
