import datetime
import time

from sqlalchemy import and_

from db import Gig, Style
from db.connect import connect_db
from services.messages import Messages
from vk.vk_connect import VkConnect


class GigService(Messages):
    def __init__(self, api: VkConnect, chat_id: int):
        self.chat_id = chat_id
        self.session = connect_db()
        super().__init__(api)

    def get_by_period(self, genre_name: str, days: int) -> None:
        genre = self._get_genre(genre_name)
        if genre:
            now = datetime.datetime.now().date()
            gigs = self.session.query(Gig).filter_by(style=genre.id).filter(
                and_(Gig.date >= now, Gig.date <= now + datetime.timedelta(days=days))).all()
            self._gig_message(gigs)

    def get_by_day(self, genre_name: str, date: str) -> None:
        try:
            date = datetime.datetime.strptime(date, "%d.%m").date().replace(year=datetime.datetime.now().year)
            genre = self._get_genre(genre_name)
            if genre:
                gigs = self.session.query(Gig).filter_by(style=genre.id).filter(Gig.date == date).all()
                self._gig_message(gigs)
        except:
            self.message(self.chat_id, 'Некорректные данные')

    def _gig_message(self, gigs):
        mess = ''
        for g in gigs:
            mess += self._one_gig(g)
        if mess == '':
            mess = 'Концерты не найдены'
        self.message(self.chat_id, mess)

    def _get_genre(self, genre_name: str) -> Style or None:
        genre = self.session.query(Style).filter_by(name=genre_name).first()
        if genre is None:
            self.message(self.chat_id, 'Жанр не найден')
        else:
            return genre

    @staticmethod
    def _one_gig(gig: Gig) -> str:
        return f'[{gig.date.strftime("%d.%m")}] {gig.name} - {gig.club or "Неизвестно"} (Цена: {gig.price}) \n'
