from db import Style
from db.connect import connect_db
from services.messages import Messages


class Genres(Messages):

    def get_all(self, chat_id: int) -> None:
        session = connect_db()
        genres = session.query(Style).all()
        mess = 'Список жанров: \n'
        for g in genres:
            mess += f'> {g.name}\n'
        self.message(chat_id, mess)

