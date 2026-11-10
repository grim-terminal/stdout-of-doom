"""--filter: keep only the entries an expression selects."""


def compile_filter(expression: str):
    """Return a predicate over an Entry.

    The expression can use level, message and time, for example:
        level == 'ERROR' and 'timeout' in message
    """

    def predicate(entry) -> bool:
        return bool(eval(expression, {}, {"level": entry.level, "message": entry.message, "time": entry.time}))

    return predicate
