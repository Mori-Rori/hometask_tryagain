import pytest
from typing import List, Dict
from main.processing import filter_by_state, sort_by_date


@pytest.mark.parametrize(
    'test_input, state, expected',
    (
        ([{'state': 'EXECUTED', 'amount': 100}, {'state': 'CANCELED', 'amount': 200}], 'EXECUTED', [{'state': 'EXECUTED', 'amount': 100}]),
        ([{'state': 'EXECUTED', 'amount': 50}, {'state': 'EXECUTED', 'amount': 150}, {'state': 'CANCELED', 'amount': 100}], 'EXECUTED', [{'state': 'EXECUTED', 'amount': 50}, {'state': 'EXECUTED', 'amount': 150}]),
        ([{'state': 'CANCELED', 'amount': 75}, {'state': 'CANCELED', 'amount': 300}], 'CANCELED', [{'state': 'CANCELED', 'amount': 75}, {'state': 'CANCELED', 'amount': 300}]),
        ([{'state': 'EXECUTED', 'amount': 10}], 'CANCELED', []),  # нет элементов с указанным состоянием
    )
)
def test_filter_by_state(test_input, state, expected):
    assert filter_by_state(test_input, state) == expected


@pytest.mark.parametrize(
    'test_input, reverse, expected',
    (
        ([{'date': '2023-10-01', 'amount': 100}, {'date': '2023-09-01', 'amount': 200}], True, [
            {'date': '2023-10-01', 'amount': 100},
            {'date': '2023-09-01', 'amount': 200}
        ]),
        ([{'date': '2023-10-01', 'amount': 50}, {'date': '2023-09-15', 'amount': 150}, {'date': '2023-09-01', 'amount': 100}], False, [
            {'date': '2023-09-01', 'amount': 100},
            {'date': '2023-09-15', 'amount': 150},
            {'date': '2023-10-01', 'amount': 50}
        ]),
        ([{'date': '2023-08-01', 'amount': 75}, {'date': '2023-07-01', 'amount': 300}], True, [
            {'date': '2023-08-01', 'amount': 75},
            {'date': '2023-07-01', 'amount': 300}
        ]),
    )
)
def test_sort_by_date(test_input, reverse, expected):
    assert sort_by_date(test_input, reverse) == expected
