import datetime
import logging

from bs4 import BeautifulSoup
import requests

from .constants import (
    RUSSIAN_LETTERS, RU_WIKI_MAIN_URL, HEADERS, INITIAL_PARSING_PAGE,
    REQUESTS_TIMEOUT, NEXT_PAGE_TEXT
)

from .utils import (
    is_letter_in_alphabet, save_dict_as_two_column_csv,
    count_items_by_alphabet_letter
)


logging.basicConfig(
    level=logging.INFO, filename='task2_log.log', filemode='w',
    format='%(asctime)s %(levelname)s %(message)s', encoding='utf8'
)


def get_all_animal_names_from_wiki() -> list[str]:
    logging.info(
        f'Начало работы ф-ции {get_all_animal_names_from_wiki.__name__}.'
    )

    start_time = datetime.datetime.now()

    animal_names = []
    category_group_h3_set = set()
    category_group_h3_not_eng_flag = True

    URL = INITIAL_PARSING_PAGE

    while URL and category_group_h3_not_eng_flag:

        try:
            response = requests.get(
                URL, headers=HEADERS, timeout=REQUESTS_TIMEOUT
            )
        except requests.exceptions.RequestException as error:
            logging.error(f'Возникла ошибка:\n{error}.')
            break

        soup = BeautifulSoup(response.text, features='lxml')

        mw_pages = soup.find('div', attrs={'id': 'mw-pages'})
        if not mw_pages:
            logging.info('Не нашлось тега mw-pages.')
            break

        mw_category_columns = mw_pages.find(
            'div', attrs={'class': 'mw-category mw-category-columns'}
        )
        if not mw_category_columns:
            logging.info('Не нашлось тега mw_category_columns.')
            break

        mw_category_groups = mw_category_columns.find_all(
            'div', attrs={'class': 'mw-category-group'}
        )
        if not mw_category_groups:
            logging.info('Не нашлось тегов mw_category_groups.')
            break

        for category_group in mw_category_groups:
            category_group_h3 = category_group.find('h3')
            if category_group_h3:
                text = category_group_h3.text.strip()
                if text:
                    if not is_letter_in_alphabet(text[0], RUSSIAN_LETTERS):
                        category_group_h3_not_eng_flag = False
                        break
                    category_group_h3_set.add(text[0])

            ul_item = category_group.find('ul')
            if not ul_item:
                continue

            li_items = ul_item.find_all('li')
            for item in li_items:
                text = item.text.strip()
                if text and is_letter_in_alphabet(
                    text[0], RUSSIAN_LETTERS
                ):
                    animal_names.append(text)

        next_page_url = mw_pages.find('a', string=NEXT_PAGE_TEXT)
        if next_page_url:
            URL = (RU_WIKI_MAIN_URL + next_page_url['href'])
        else:
            break

    end_time = datetime.datetime.now()

    logging.info(
        f'Конец работы ф-ции {get_all_animal_names_from_wiki.__name__}.\n'
        f'Найдено количество названий: {len(animal_names)}.\n'
        f'Найдены теги h3: {category_group_h3_set}.\n'
        f'Парсинг был выполнен за время: {end_time - start_time}.')

    return animal_names


if __name__ == '__main__':
    parsing_data = get_all_animal_names_from_wiki()
    count_result = count_items_by_alphabet_letter(
        parsing_data, RUSSIAN_LETTERS
    )
    save_dict_as_two_column_csv(
        count_result, ['Буква', 'Количество'], 'count_result.csv'
    )
