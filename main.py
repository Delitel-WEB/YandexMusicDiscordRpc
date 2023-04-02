from presence import cfg
from presence.YM.track import Track
from presence.YM import get_current_track
from presence.YM.handlers import trackNotFoundHandler
from pypresence import Presence
from time import sleep, time

trackTime: float = None
lastTrack: Track = None

rpc = Presence(cfg.app_id)
rpc.connect()

@trackNotFoundHandler
def main():
    global lastTrack, trackTime

    while True:
        currentTrack = get_current_track()
        currentTime = time()
        if lastTrack != currentTrack:
            lastTrack = currentTrack
            trackTime = currentTime
        remainingTime = int(currentTrack.duration_sec - (currentTime - trackTime))
        rpc.update(
            state=currentTrack.name,
            details=', '.join(currentTrack.artists),
            large_image=currentTrack.preview,
            start=trackTime,
            buttons=[{"label": "Слушать", "url": currentTrack.link}],
            end=currentTime + remainingTime
        )
        sleep(20)


main()