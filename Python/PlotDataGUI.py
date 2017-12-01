from appJar import gui
from os import walk
import csv
#import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

def plot(fn):
    mdata = pd.read_csv('data/'+fn)
    tmp = mdata['-999.999'].values.tolist()
    #determine start time...
    started = False #we have not started the data recording yet
    mvec = []
    for x in tmp:
        if x <-10 and started == False:
            continue
        elif x > -10 and started == False:
            started = True
        if started == True:
            mvec.append(x)
    plt.figure(1)
    plt.plot(mvec)
    plt.title('Laser Measurements')
    plt.ylabel('Distance from laser (mm)')
    plt.xlabel('Number of samples')
    plt.grid('on')
    plt.show()
    return

def press(button):
    if button == "Exit":
        app.stop()
    else:
        fn = app.getOptionBox("File Name")
        plot(fn)
        print"Plotting: " + fn


if __name__ == '__main__':
    app = gui("Selection Window","500x200")
    app.setBg("orange")

    app.addLabel("title", "Welcome to the selector!")
    app.setLabelBg("title", "Blue")
    app.setLabelFg("title", "Orange")
    
    app.setFont(12)
    mypath = ".\data"
    files = []
    for (dirpath, dirnames, filenames) in walk(mypath):
        files.extend(filenames)
        break

    app.addLabelOptionBox("File Name",files)

    app.addButtons(["Plot","Exit"], press)

    app.go()
