from typing import List

n = [3, 5, 7]


def list_extender(l: List[int]) -> List[int]:
    new_list = l.copy()
    new_list.append(9)
    return new_list

# 注释掉所有 print，让测试框架自己处理
# print(list_extender(n))
# print(n)
