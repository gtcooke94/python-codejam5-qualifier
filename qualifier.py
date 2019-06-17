import random
import string
import string
import random


def generate_password(
    password_length: int = 8,
    has_symbols: bool = False,
    has_uppercase: bool = False,
    ignored_chars: list = None,
    allowed_chars: list = None,
) -> str:
    """Generates a random password.

    The password will be exactly `password_length` characters.
    If `has_symbols` is True, the password will contain at least one symbol, such as #, !, or @.
    If `has_uppercase` is True, the password will contain at least one upper case letter.
    `ignored_chars` is a list that, if supplied, will cause the password to not contain those characters.
    `allowed_chars` is a list that, if supplied, will cause the password to only contain characters in the list.
    """

    if ignored_chars and allowed_chars:
        raise UserWarning("Only one of ignored_chars and allowed_chars is allowed. Both were supplied.")
    all_allowed = set(string.ascii_lowercase)
    symbols = set("#!@")
    uppercase = set(string.ascii_uppercase)
    if ignored_chars:
        ignored_chars = set(ignored_chars)
        symbols -= ignored_chars
        uppercase -= ignored_chars
        all_allowed -= ignored_chars
    if allowed_chars:
        allowed_chars = set(allowed_chars)
        symbols &= allowed_chars
        uppercase &= allowed_chars
        all_allowed &= allowed_chars

    password = []
    if has_symbols:
        password.append(random.sample(symbols, 1)[0])
    if has_uppercase:
        password.append(random.sample(uppercase, 1)[0])
    all_allowed |= uppercase
    all_allowed |= symbols
    all_allowed = list(all_allowed)
    remaining_length = password_length - has_symbols - has_uppercase
    password.extend(random.choices(all_allowed, k=remaining_length))
    random.shuffle(password)
    return "".join(password)
