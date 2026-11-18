from typing import List

n = [3, 5, 7]


def list_extender(l: List[int]) -> List[int]:
    new_list = l.copy()
    new_list.append(9)
    return new_list


# 只保留这一行
print(list_extender(n))
