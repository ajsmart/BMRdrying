from appJar import gui

def press(button):
    if button == "Exit":
        app.stop()
    else:
        val = app.getEntry("File Name:")
        #the commented out code was an experiment that worked.  I'm leaving it here for future reference
        #app.setLabel("message","You just started recording")
        if val =="":
            app.setLabel("message","Error: No filename Designated")
            app.setLabelBg("message","red")
            app.setLabelFg("message","green")
        else:
            app.setLabel("message","Starting measurement program!")
            app.setLabelBg("message","Green")
            app.setLabelFg("message","Black")

if __name__ == '__main__':
    #initiate app
    app = gui("Scale Window","500x200")
    app.setBg("green")
    app.setFont(12)

    #title panel
    app.addLabel("title","Scale Reading System", colspan=2)
    app.setLabelBg("title","blue")
    app.setLabelFg("title","green")

    #Filename input
    row = app.getRow()
    app.addLabelEntry("File Name:",row,0)
    app.addLabel(".csv",".csv",row,1)

    #declare buttons
    app.addButtons(["Start Measurements","Exit"],press, colspan=2)

    #message area
    app.addLabel("message","", colspan=2)
    #app.setLabelFg("message","Red")

    app.go()
