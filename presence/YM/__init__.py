from yandex_music import Client
from ..cfg import ym_id
from .track import Track
from ..utils import ms_to_sec

YM_CLIENT = Client(ym_id).init()


def get_current_track():
    queues = YM_CLIENT.queues_list()
    currentQueue = YM_CLIENT.queue(queue_id=queues[0].id)
    currentTrack = currentQueue.get_current_track()
    aboutTrack = currentTrack.fetch_track()

    return Track(
        [artist.name for artist in aboutTrack.artists],
        aboutTrack.title,
        "https://" + aboutTrack.cover_uri.replace("%%", "200x200"),
        f"https://music.yandex.ru/album/{aboutTrack.albums[0].id}/track/{aboutTrack.id}",
        ms_to_sec(aboutTrack.duration_ms)
    )
