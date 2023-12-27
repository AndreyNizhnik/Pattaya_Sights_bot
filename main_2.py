import requests
from pprint import pprint
import time
from datetime import datetime as dt

TG_URL = "https://api.telegram.org/bot{}/{}"
TOKEN = "6744015199:AAHqC9-0Oobb3PeKwhG45mXJylXJmSkqI2A"

offset = 0


def message_mirror(message):
    chat_id = message.get('message',{}).get('from').get('id')
    message_text = message.get('message',{}).get('text')
    is_photo = message.get('message',{}).get('photo')
    is_sticker = message.get('message',{}).get('sticker')
    is_voice = message.get('message',{}).get('voice')

    if message_text:
        requests.post(url=TG_URL.format(TOKEN, 'sendMessage'),
                      data={'chat_id': chat_id,
                            'text': f"Your message was received:\n"
                                    f"'{message_text}'"
                            })
    elif is_photo:
        requests.post(url=TG_URL.format(TOKEN, 'sendMessage'),
                      data={'chat_id': chat_id,
                            'text': f"Your photo was received!"
                            })

    elif is_sticker:
        requests.post(url=TG_URL.format(TOKEN, 'sendMessage'),
                      data={'chat_id': chat_id,
                            'text': f"Nice sticker!"
                            })

    elif is_voice:
        requests.post(url=TG_URL.format(TOKEN, 'sendMessage'),
                      data={'chat_id': chat_id,
                            'text': f"Your voice message is received!"
                            })

# =====================================================================================
# main loop


while True:
    response = requests.get(url=TG_URL.format(TOKEN, 'getUpdates'),
                            params={'offset': offset})

    if response.ok:
        data = response.json()['result']
        now = dt.now()
        current_time = now.strftime("%H:%M:%S")
        pprint(f"update {current_time} : {data}")
        try:
            offset = data[-1]['update_id']+1
        except IndexError:
            time.sleep(1)
            pass
        for i in data:
            message_mirror(i)
