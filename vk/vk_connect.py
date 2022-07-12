import os

import vk_api
from vk_api.bot_longpoll import VkBotLongPoll
from vk_api.utils import get_random_id
from dotenv import load_dotenv
load_dotenv()


class VkConnect:

    def __init__(self) -> None:
        self.group_id = os.getenv('VK_GROUP_ID')
        self.vk_session = vk_api.VkApi(token=os.getenv('VK_TOKEN'))
        self.longpoll = VkBotLongPoll(self.vk_session, self.group_id)
        self.api = self.vk_session.get_api()

    def send_message(self, text: str, chat_id: int, disable: bool = False) -> None:
        self.api.messages.send(
            random_id=get_random_id(),
            message=text,
            chat_id=chat_id,
            disable_mentions=disable
        )
