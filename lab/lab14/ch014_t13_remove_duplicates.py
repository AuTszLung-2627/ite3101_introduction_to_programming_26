from typing import List


def remove_duplicates(seq: List[int]) -> List[int]:
    result = []
    for item in seq:
        if utem not in result:
            result.append(item)
    return result
