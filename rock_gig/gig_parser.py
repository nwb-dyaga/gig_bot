import os
import time

from dotenv import load_dotenv

from db import Style, Gig
from db.connect import connect_db
from db.utils import get_or_create
from parser.parser import Parser
from utils.make_request import make_request

load_dotenv()


class RockGigApi:

    def __init__(self) -> None:
        self.session = connect_db()

    def get_all_genres(self) -> None:
        genres = self.session.query(Style).all()
        for genre in genres:
            self.get_all_pages(genre.screen_name)
            time.sleep(10)

    def get_all_pages(self, genre: str) -> None:
        iter = 0
        while True:
            data = make_request(self._style_url(iter, genre))
            if data is None:
                return
            if 'esMiss' in str(data):
                return
            else:
                self.get_one_page(data, genre)
            iter += 1

    def get_one_page(self, data: str, genre: str) -> None:
        parser = Parser(data)
        for gig in parser.find_gig():
            defaults = {
                'price': parser.find_price(gig),
                'date': parser.find_date(gig),
                'club': parser.find_club(gig),
                'groups': parser.find_bands(gig),
            }
            self.get_or_create_gig(genre, defaults, parser.find_name(gig), parser.find_id(gig))

    @staticmethod
    def _style_url(i: int, genre: str) -> str:
        return f'{os.getenv("DEFAULT_URL")}tag/{genre}/page{i}'

    def get_or_create_gig(self, style_name: str, defaults: dict, name: str, gig_id: str) -> None:
        style = self.session.query(Style).filter_by(screen_name=style_name).first()
        get_or_create(self.session, Gig, defaults=defaults, name=name, style=style.id, gig_id=gig_id)
