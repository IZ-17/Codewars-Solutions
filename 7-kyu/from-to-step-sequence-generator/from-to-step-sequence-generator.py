def generator (_from, _to, _step):
    if _step == 0:
        return []
    return [num for num in range(_from, _to + 1, _step)] if _from < _to else [num for num in range(_from, _to - 1, -_step)]