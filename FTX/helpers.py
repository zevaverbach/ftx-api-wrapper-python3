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
    if 'side_required' in kwargs and kwargs['side_required'] not in ("buy", "sell"):
        raise exceptions.Invalid(f"'side' should be one of 'buy' or 'sell'")

    if 'type_' in kwargs and kwargs['type_'] not in (None, "stop", "trailing_stop", "take_profit"):
        raise exceptions.Invalid("'type_' must be one of 'stop', 'trailing_stop', or 'take_profit'")
    if 'type_required' in kwargs and kwargs['type_required'] not in ("limit", "market"):
        raise exceptions.Invalid("'type_' should be one of 'limit' or 'market'")
    if 'order' in kwargs and kwargs['order'] not in (None, "asc"):
        raise exceptions.Invalid("Please supply either None or 'asc' for `order`")
    VALID_CHAINS = (None, "omni", "erc20", "trx", "sol", "bep2")
    if 'chain' in kwargs and kwargs['chain'] not in VALID_CHAINS:
        raise exceptions.Invalid(f"'chain' must be in {', '.join(constants.VALID_CHAINS)}")

    VALID_K_LINE_RESOLUTIONS = (15, 60, 300, 900, 3600, 14400, 86400)
    if 'resolution' in kwargs and kwargs['resolution'] not in VALID_K_LINE_RESOLUTIONS:
        raise exceptions.Invalid(
            f"resolution must be in {', '.join(VALID_K_LINE_RESOLUTIONS)}"
        )
    if 'depth' in kwargs and kwargs['depth'] > 100 or kwargs['depth'] < 20:
        raise exceptions.Invalid("depth must be between 20 and 100")
