from pypresence import Presence
from presence.YM import get_current_track
from presence import cfg
from time import sleep, time
from presence.YM.track import Track

trackTime: float = None
lastTrack: Track = None

rpc = Presence(cfg.app_id)
rpc.connect()


def main():
    global lastTrack, trackTime

    while True:
        currentTime = time()
        currentTrack = get_current_track()
        if lastTrack != currentTrack:
            lastTrack = currentTrack
            trackTime = time()
        remainingTime = int(currentTrack.duration_sec - (currentTime - trackTime))
        rpc.update(
            state=currentTrack.name,
            details=', '.join(currentTrack.artists),
            large_image=currentTrack.preview,
            start=trackTime,
            buttons=[{"label": "Слушать", "url": currentTrack.link}],
            end=currentTime + remainingTime
        )
        sleep(1)


main()