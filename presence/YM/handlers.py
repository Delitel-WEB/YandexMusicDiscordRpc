from yandex_music.exceptions import NotFoundError
from time import sleep


def trackNotFoundHandler(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except (NotFoundError, IndexError):
            print("Активный трек не обнаружен или очередь пуста!")
            sleep(20)
            return wrapper(*args, **kwargs)

    return wrapper
