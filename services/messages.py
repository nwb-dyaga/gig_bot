from vk.vk_connect import VkConnect


class Messages:
    def __init__(self, api: VkConnect) -> None:
        self.api = api

    def message(self, chat_id: int, mess: str) -> None:
        self.api.send_message(
            text=mess,
            chat_id=chat_id
        )