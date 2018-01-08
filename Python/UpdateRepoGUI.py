import subprocess
import datetime
from appJar import gui
import os


def commit(button):
    if button == "Exit":
        app.stop()
    upd8 = "git pull"
    add = "git add --all"
    now = datetime.datetime.now()
    year = str(now.year)
    month = str(now.month)
    day = str(now.day)
    hour = str(now.hour)
    minute = str(now.minute)
    commit = "git commit -m \"automated python git update" + month + "-" + day + "-" + year + " " + hour + ":" + minute +"\""
    push = "git push origin master"
    os.system(upd8)
    os.system(add)
    os.system(commit)
    os.system(push)
#######################################
if __name__ == '__main__':
    app = gui("Selection Window","500x200")
    app.setBg("PaleTurquoise")
    app.setFont(12)

    app.addLabel("title", "Push data to GIT repository.")
    app.setLabelBg("title", "Black")
    app.setLabelFg("title", "PaleTurquoise")

    app.addButtons(["Push","Exit"], commit)

    app.go()