import os
import pystray
from PIL import Image

from recording import *


def systemTray(onLive):
    path = os.path.abspath(os.path.dirname(__file__))
    ico_folder = os.path.expanduser(path)

    def after_click(icon, query):
        if str(query) == "Exit":
            icon.stop()

    if onLive:
        image = Image.open(os.path.join(ico_folder, "rec2button.png"))
        print("onLive true")
    elif onLive == 0:
        image = Image.open(os.path.join(ico_folder, "recbutton.png"))
        print("onLive false")

    icon = pystray.Icon("sr", image, "ScreenRecorder",
                        menu=pystray.Menu(pystray.MenuItem("Exit", after_click)))
    icon.update_menu()
    icon.run()