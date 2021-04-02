import pafy
#import vlc
"""
pip install python-vlc
pip install youtube-dl
pip install pafy
"""


try:
    url = "https://www.youtube.com/watch?v=bMt47wvK6u0"
    video = pafy.new(url)
    best = video.getbest()
    playurl = best.url
    best.download(quiet=False)
    filename = best.download(filepath="/tmp/Game."+best.extension)
except:
    print('pafy module')

"""
try:
    Instance = vlc.Instance()
    player = Instance.media_player_new()
    Media = Instance.media_new(playurl)
    Media.get_mrl()
    player.set_media(Media)
    player.play()
except:
    print('vlc prob')

"""