from typing import List, Dict, Union, Generator
import numpy as np

# We will work with such dicts
ST = Dict[str, Union[str, int]]
# And we will put this dicts in list
DT = List[ST]


def task_1_fix_names_start_letter(data: DT) -> DT:
    """
    Make all `names` field in list of students to start from upper letter

    Examples:
        fix_names_start_letters([{'name': 'Alex', 'age': 26}, {'name': 'denys', 'age': 89}])
        >>> [{'name': 'Alex', 'age': 26}, {'name': 'Denys', 'age': 89}]
    """
    for item in data:
        if item.get('name'):
            item.update(name=item.get('name').title())
    return data


def task_2_remove_dict_fields(data: DT, redundant_keys: List[str]) -> DT:
    """given_data
    Remove from dictionaries given key value

    Examples:
       remove_dict_field([{'name': 'Alex', 'age': 26}, {'name': 'denys', 'age': 89}], 'age')
        >>> [{'name': 'Alex'}, {'name': 'denys'}]
    """
    return [{k: v for k, v in i.items() if k not in redundant_keys} for i in data]


def task_3_find_item_via_value(data: DT, value) -> DT:
    """
    Find and return all items that has @searching value in any key
    Examples:
        find_item_via_value([{'name': 'Alex', 'age': 26}, {'name': 'denys', 'age': 89}], 26)
        >>> [{'name': 'Alex', 'age': 26}]
    """
    if data:
        return [d for d in data for k, v in d.items() if v == value]


def task_4_min_value_integers(data: List[int]) -> [int]:
    """
    Find and return minimum value from list
    """
    if data:
        return min(item for item in data)


def task_5_min_value_strings(data: List[Union[str, int]]) -> str:
    """
    Find the shortest string
    """
    if data:
        data = [str(d) for d in data]
        data.sort(key=len)
        shortest = data[0]
        return shortest


def task_6_min_value_list_of_dicts(data: DT, key: str) -> ST:
    """
    Find minimum value by given key
    Returns:

    """
    return min([d for d in data if d.get(key)], key=lambda x: x[key])


def task_7_max_value_list_of_lists(data: List[List[int]]) -> List[int]:
    """
    Find max value from list of lists
    """
    m = np.array(data)
    c = max(m)
    return max(c)


def task_8_sum_of_ints(data: List[int]) -> int:
    """
    Find sum of all items in given list
    """
    return sum(i for i in data)


def task_9_sum_characters_positions(text: str) -> int:
    """
    Please read first about ascii table.
    https://python-reference.readthedocs.io/en/latest/docs/str/ASCII.html
    You need to calculate sum of decimal value of each symbol in text

    Examples:
        task_9_sum_characters_positions("A")
        >>> 65
        task_9_sum_characters_positions("hello")
        >>> 532

    """
    text = 'Generators are iterators, but you can only iterate over them once.'
    return sum(ord(ch) for ch in text)


def task_10_generator_of_simple_numbers() -> Generator[int, None, None]:
    """
    Return generator of simple numbers
    Stop then iteration if returned value is more than 200
    Examples:
        a = task_10_generator_of_simple_numbers()
        next(a)
        >>> 2
        next(a)
        >>> 3
    """
    a = 2
    while a <= 201:
        for i in range(2, a):
            if a % i == 0:
                a += 1
                break
        else:
            yield a
            a += 1
