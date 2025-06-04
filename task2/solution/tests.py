import csv
import os
from unittest.mock import patch, Mock
import unittest

from .constants import RUSSIAN_LETTERS
from .parse_animal_names import get_all_animal_names_from_wiki
from .utils import count_items_by_alphabet_letter, save_dict_as_two_column_csv


class TestParseAnimalNames(unittest.TestCase):
    @patch('solution.parse_animal_names.requests.get')
    def test_parse_counting_saving(self, mock_get):
        mock_html = '''
        <div id="mw-pages">
            <div class="mw-category mw-category-columns">
                <div class="mw-category-group">
                    <h3>А</h3>
                    <ul>
                        <li>Аист</li>
                        <li>   Антилопа</li>
                    </ul>
                </div>
                <div class="mw-category-group">
                    <h3>Б</h3>
                    <ul>
                        <li>Бобр</li>
                        <li>Бык   </li>
                    </ul>
                </div>
                <div class="mw-category-group">
                    <h3>F</h3>
                    <ul>
                        <li>Frog</li>
                        <li>Fox</li>
                    </ul>
                </div>
                <div class="mw-category-group">
                    <h3>F</h3>
                    <ul>
                        <li>Корова</li>
                        <li>Кот</li>
                    </ul>
                </div>
            </div>
            <a href="/wiki/Следующая_страница">Следующая страница</a>
        </div>
        '''
        mock_response = Mock()
        mock_response.text = mock_html
        mock_get.return_value = mock_response

        with patch(
                'solution.parse_animal_names.INITIAL_PARSING_PAGE',
                'https://example.com'
        ):
            with patch(
                    'solution.parse_animal_names.RU_WIKI_MAIN_URL',
                    'https://example.com'
            ):
                with patch('solution.parse_animal_names.HEADERS', {}):
                    with patch(
                            'solution.parse_animal_names.REQUESTS_TIMEOUT', 5
                    ):
                        animal_names = get_all_animal_names_from_wiki()

        self.assertEqual(animal_names, ['Аист', 'Антилопа', 'Бобр', 'Бык'])

        test_data = count_items_by_alphabet_letter(
            animal_names, RUSSIAN_LETTERS
        )

        self.assertEqual(test_data, {'А': 2, 'Б': 2})

        test_csv_filename = 'test_output.csv'
        if os.path.exists(test_csv_filename):
            os.remove(test_csv_filename)

        save_dict_as_two_column_csv(
            test_data, ['Буква', 'Количество'], test_csv_filename
        )

        self.assertTrue(os.path.exists(test_csv_filename))

        with open(test_csv_filename, encoding='utf-8') as f:
            reader = list(csv.reader(f))
            self.assertEqual(reader[0], ['Буква', 'Количество'])
            self.assertIn(['А', '2'], reader)
            self.assertIn(['Б', '2'], reader)


if __name__ == '__main__':
    unittest.main()
