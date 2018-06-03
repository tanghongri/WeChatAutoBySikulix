import org.sikuli.script.SikulixForJython
from sikuli import *
import json

# using an existing window if possible
myApp = App("WeChat")
if not myApp.window():  # no window(0) - Firefox not open
    App.open('"C:\\Program Files (x86)\\Tencent\\WeChat\\WeChat.exe"')
    wait(2)
myApp.focus()

if __name__ == "__main__":
    print(1)