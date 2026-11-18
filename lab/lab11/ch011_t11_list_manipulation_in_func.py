from typing import List

n = [3, 5, 7]
# Add your function here


def list_extender(l: List[int]) -> List[int]:
    new_list = l.copy()
    new_list.append(9)
    return new_list


print(list_extender(n))
print(n)
