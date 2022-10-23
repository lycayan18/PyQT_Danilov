import cryptocode


def encode(text: str, key: str) -> str:
    """Кодирование текста"""
    return cryptocode.encrypt(text, key)


def decode(text: str, key: str) -> str:
    """Декодирование текста"""
    return cryptocode.decrypt(text, key)
