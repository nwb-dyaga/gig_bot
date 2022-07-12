from datetime import datetime

import requests
from vk_api.bot_longpoll import VkBotEventType

from services.commands_service import Commands
from services.genres import Genres
from services.gig_service import GigService
from vk.vk_connect import VkConnect

vk = VkConnect()

while True:
    try:
        for event in vk.longpoll.listen():
            if event.type == VkBotEventType.MESSAGE_NEW:
                if event.from_chat:
                    peer_id = event.object.message['peer_id']
                    command = event.object.message['text'].split()
                    if '[club214474746|@gig_bot]' in command or '[club214474746|*gig_bot]' in command:
                        if 'команды' in command:
                            Commands(vk).get_all(event.chat_id)
                        elif 'месяц' == command[-1]:
                            GigService(vk, event.chat_id).get_by_period(command[-2], 30)
                        elif 'неделя' == command[-1]:
                            GigService(vk, event.chat_id).get_by_period(command[-2], 7)
                        elif '.' in command[-1]:
                            GigService(vk, event.chat_id).get_by_day(command[-2], command[-1])
                        elif 'жанры' in command:
                            Genres(vk).get_all(event.chat_id)
                        else:
                            Commands(vk).get_all(event.chat_id)
    except requests.exceptions.ReadTimeout:
        pass
