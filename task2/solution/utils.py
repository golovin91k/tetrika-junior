from collections import Counter
from collections.abc import Iterable
import csv


def is_letter_in_alphabet(
        letter: str, alphabet: Iterable[str]) -> bool:
    return letter in alphabet


def save_dict_as_two_column_csv(
        data: dict[str, int],
        headers: list[str],
        filename: str):
    with open(filename, 'w', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(headers)
        for col_1, col_2 in data.items():
            writer.writerow([col_1, col_2])


def count_items_by_alphabet_letter(
        items: list[str], alphabet: Iterable[str]
) -> dict:
    result = []
    first_letters = []
    for item in items:
        first_letters.append(item[0])
    counter = Counter(first_letters)
    for letter in alphabet:
        if letter in counter:
            result.append((letter, counter[letter]))
    return dict(result)
