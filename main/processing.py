from typing import Dict, List


def filter_by_state(data: List[Dict], state: str = 'EXECUTED') -> List[Dict]:
    """
    Фильтрует список словарей по значению ключа 'state'.

    :param data: Список словарей для фильтрации.
    :param state: Значение ключа 'state', по умолчанию 'EXECUTED'.
    :return: Новый список словарей, соответствующих указанному значению ключа 'state'.
    """
    return [item for item in data if item.get('state') == state]


def sort_by_date(data: List[Dict], reverse: bool = True) -> List[Dict]:
    """
    Сортирует список словарей по дате.

    :param data: Список словарей для сортировки.
    :param reverse: Параметр, задающий порядок сортировки. По умолчанию True (убывание).
    :return: Новый отсортированный список словарей.
    """
    return sorted(data, key=lambda x: x['date'], reverse=reverse)
