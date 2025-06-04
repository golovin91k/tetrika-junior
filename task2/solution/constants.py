CAPITAL_RUSSIAN_LETTERS = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
LOWERCASE_RUSSIAN_LETTERS = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'

RUSSIAN_LETTERS = CAPITAL_RUSSIAN_LETTERS + LOWERCASE_RUSSIAN_LETTERS

RU_WIKI_MAIN_URL = 'https://ru.wikipedia.org'

INITIAL_PARSING_PAGE = (
        'https://ru.wikipedia.org/wiki/'
        '%D0%9A%D0%B0%D1%82%D0%B5%D0%B3%D0%BE%D1%80%D0%B8%D1%8F:'
        '%D0%96%D0%B8%D0%B2%D0%BE%D1%82%D0%BD%D1%8B%D0%B5_%D0%BF%D0%BE_'
        '%D0%B0%D0%BB%D1%84%D0%B0%D0%B2%D0%B8%D1%82%D1%83'
)

HEADERS = {'User-Agent': 'Mozilla/5.0'}

REQUESTS_TIMEOUT = 10

NEXT_PAGE_TEXT = 'Следующая страница'
