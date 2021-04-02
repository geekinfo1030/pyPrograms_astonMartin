import urllib.request
import re
url = ''
#html = urllib.request.urlopen(url)

#video_urls = re.findall()

import os
os.environ['PYTHON_VLC_MODULE_PATH'] = """C:\Program Files (x86)\VideoLAN\VLC"""
os.environ['PYTHON_VLC_LIB_PATH'] = """C:\Program Files (x86)\VideoLAN\VLC"""
# now you can import vlc
import vlc

