from typing import Any


def distance_foem_zero(d: Amy) -> Any:
    if type(d) == int or type(d) == float:
        return abs(d)
    return "Nope"
