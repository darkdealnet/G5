
def value_validate(value) -> tuple:
    len_value = len(value)
    firs_char = value[:1]

    if len_value > 30:
        return None, False, f"value is large {len_value}"
    elif firs_char == "+":
        if value[1:].isdigit():
            return value[1:], True, None
        else:
            return None, False, f"incorrect value"
    elif firs_char == "-":
        return None, False, f"negative number"
    else:
        if value.isdigit():
            return value, True, None
        else:
            return None, False, f"incorrect value"
