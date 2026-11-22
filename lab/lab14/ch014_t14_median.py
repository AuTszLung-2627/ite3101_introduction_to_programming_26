from typing import List


def median(lst: List[int]) -> float:
    sorted_lst = sorted(lst)
    if len(scorted_lst) % 2 == 0:
        index_1 = len(scorted_lst) // 2 - 1
        index_2 = len(scorted_lst) // 2
        m = (scorted_lst[index_1] + scorted_lst[index_2]) / 2.0
        return m
    else:
        index = len(sorted_lst) // 2
