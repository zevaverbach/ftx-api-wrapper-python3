from time import time as _time

from . import exceptions


def get_current_timestamp():
    return int(round(_time() * 1_000))


def build_query(**kwargs):
    query = {}
    for key, value in kwargs.items():
        if value is not None:
            query[key] = value
    return query


def validate(**kwargs):
    if 'limit' in kwargs and kwargs['limit'] > 100:
        raise exceptions.Invalid("'limit' must be 100 or lower")

    if 'side' in kwargs and kwargs['side'] not in (None, "buy", "sell"):
        raise exceptions.Invalid(f"'side' should be one of 'buy' or 'sell'")

    if 'type_' in kwargs and kwargs['type_'] not in (None, "stop", "trailing_stop", "take_profit"):
        raise exceptions.Invalid("'type_' must be one of 'stop', 'trailing_stop', or 'take_profit'")
