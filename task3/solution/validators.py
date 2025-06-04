from .exceptions import ValidationError


def check_type_timestamp(
        value: int, position: int, key_name: str,
) -> None:
    if type(value) is not int:
        raise ValidationError(
            f'Временная метка {value} (позиция {position}) ключа '
            f'"{key_name}" не является целым числом.'
        )


def validate_input_intervals(incoming_intervals: dict[str, list[int]]) -> None:
    if (
        not incoming_intervals.get('lesson')
        or not incoming_intervals.get('pupil')
        or not incoming_intervals.get('tutor')
    ):
        raise ValidationError(
            'Не указаны временные метки для одного из ключей.'
        )

    if len(incoming_intervals.get('lesson')) != 2:
        raise ValidationError(
            'Указано недопустимое количество временных меток для ключа'
            ' "lesson": временных меток должно быть ровно две.'
        )

    for name, intervals in incoming_intervals.items():
        if len(intervals) % 2 != 0:
            raise ValidationError(
                'Указано нечетное количество временных меток для ключа '
                f'"{name}".'
            )

        for i in range(0, len(intervals), 2):

            check_type_timestamp(intervals[i], i, name)
            check_type_timestamp(intervals[i+1], i+1, name)

            if intervals[i] > intervals[i+1]:
                raise ValidationError(
                    f'Интервал между временными метками: {intervals[i]} - '
                    f'{intervals[i+1]} (позиции № {i} и № {i+1} ключа "{name}"'
                    ' соответственно), не является положительым. '
                    'Проверьте временные метки.'
                )
