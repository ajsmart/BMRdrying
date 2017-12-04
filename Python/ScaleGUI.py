from appJar import gui

def press(button):
    if button == "Exit":
        app.stop()
    else:
        val = app.getEntry("File Name:")
        print "reading scale! " + val

if __name__ == '__main__':
    #initiate app
    app = gui("Scale Window","500x200")
    app.setBg("green")
    app.setFont(12)

    #title panel
    app.addLabel("title","Scale Reading System")
    app.setLabelBg("title","blue")
    app.setLabelFg("title","green")

    #Filename input
    app.addLabelEntry("File Name:")

    #declare buttons
    app.addButtons(["Read Scale","Exit"],press)

    app.go()
