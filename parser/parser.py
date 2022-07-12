from bs4 import BeautifulSoup, PageElement


class Parser:

    def __init__(self, content: str) -> None:
        self.soup = BeautifulSoup(content, "lxml")
        self.groups = None

    def find_gig(self):
        return self.soup.find_all(class_='el BG0')

    @staticmethod
    def find_name(gig: PageElement) -> str:
        return gig.find('div', class_='elName').a.text

    @staticmethod
    def find_price(gig: PageElement) -> str or None:
        price_div = gig.find('div', class_='os iTime eD')
        if price_div is None:
            return None
        if price_div.a is not None:
            return price_div.a.text
        elif price_div.span is not None:
            return price_div.span.text
        else:
            return price_div.text.split('₽')[-1].replace(' ', '').strip()

    @staticmethod
    def find_club(gig: PageElement) -> str:
        try:
            return gig.find('div', class_='elClub').a.text
        except:
            return None

    @staticmethod
    def find_id(gig: PageElement):
        return gig['id'].replace('EI', '')

    @staticmethod
    def find_bands(gig: PageElement) -> str:
        try:
            return gig.find('div', class_='ob elBand').text
        except:
            return None

    @staticmethod
    def find_date(gig: PageElement) -> str:
        return gig.find('div', class_='elDate').div.a['href'].split('/')[-1]
