from services.messages import Messages


class Commands(Messages):
    COMMANDS = """
    СПИСОК КОМАНД:\n
    @gig_bot, <жанр> месяц - все концерты жанра на ближайший месяц;
    @gig_bot, <жанр> неделя - все концерты жанра на ближайшую неделю;
    @gig_bot, <жанр> <дата дд.мм> - все концерты жанра дату;
    @gig_bot, команды - команды;
    """

    def get_all(self, chat_id: int) -> None:
        self.message(chat_id, self.COMMANDS)

