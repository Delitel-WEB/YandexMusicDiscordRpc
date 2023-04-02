from yandex_music import Client
from ..cfg import ym_id
from .track import Track
from ..utils import format_time, ms_to_sec
import asyncio

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
        format_time(aboutTrack.duration_ms),
        ms_to_sec(aboutTrack.duration_ms)
    )
