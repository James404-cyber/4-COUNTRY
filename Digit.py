import os, platform
try:
    import requests
except:
    os.system('pip2 install requests')

import requests
bit = platform.architecture()[0]
if bit == '64bit':
    from ik import _site_view_
   _site_view_()
elif bit == '32bit':
    from libfour import menu
    menu()
