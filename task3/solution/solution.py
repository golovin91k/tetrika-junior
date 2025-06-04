from .constants import tests
from .validators import validate_input_intervals


def create_set(intervals: list[int]) -> set:
    output_set = set()
    for i in range(0, len(intervals), 2):
        output_set.update({x for x in range(intervals[i], intervals[i+1])})
    return output_set


def appearance(intervals: dict[str, list[int]]) -> int:
    validate_input_intervals(intervals)
    lesson_set = create_set(intervals.get('lesson'))
    pupil_set = create_set(intervals.get('pupil'))
    tutor_set = create_set(intervals.get('tutor'))
    return len(lesson_set & pupil_set & tutor_set)


if __name__ == '__main__':
    for i, test in enumerate(tests):
        test_answer = appearance(test['intervals'])
        assert test_answer == test['answer'], (
            f'Error on test case {i}, got {test_answer}, '
            f'expected {test["answer"]}'
        )
