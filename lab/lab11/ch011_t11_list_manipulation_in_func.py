from typing import list

n = [3, 5, 7]


def list_extender(l: list[int]) -> list[int]:
    l.append(9)
    return l


print(list_extender(n))
print(n)
