from appJar import gui
from readScale import getdata
from readScale import close
from readScale import take_measurements
import multiprocessing
import time
import matplotlib.pyplot as plt
import csv

def readfile():
    global w1,w2,w3,d1,d2,d3
    global name
    data=pd.read_csv('data/por/'+name+'.csv')
    weightvec=data['WEIGHT'].values.tolist()
    disvec=data['DISTANCE'].values.tolist()
    w1,w2,w3=weightvec[0],weightvec[1],weightvec[2]
    d1,d2,d3=disvec[0],disvec[1],disvec[2]
##################################    
def gatherdata(button):
    #set communication between processes and input variable data
    parent_conn, child_conn = multiprocessing.Pipe()
    timelimit = 60*60*3
    tmp = app.getLabel("total_w")
    twstr = ""
    for x in tmp:
        if x == " ":
             break
        else:
            twstr = twstr + x
    tot_w = float(twstr)
    
    #multithread the timer and the scale weight
    p1 = multiprocessing.Process(target=close, args=(timelimit,)) #timer
    p2 = multiprocessing.Process(target=take_measurements, args=(child_conn,)) #data acquisition
    p1.start() #start timer
    p2.start()
    #declare result vectors
    numvec = []
    numvec2 = []
    t = []
    app.addLabel("output","")
    #collect data while time counts down.
    while p1.is_alive():
        dat = parent_conn.recv()
        app.setLabel("output",str(dat)+" grams")
        numvec.append(dat - tot_w)
        a = time.clock()
        t.append(a)
        #porosity estimate
        numvec2.append(float(((dat - tot_w)/.7893)/(3.141592*1*.06)))
    #time's up, terminate all processes
    p2.terminate()
    
    #save the data
    name = app.getEntry("File Name:")
    with open('data/Scale/'+name+'.csv', 'wb') as output:
        writer = csv.writer(output,delimiter=',')
        writer.writerow(["TIME","WEIGHT","POROSITY"])
        for x in range(0,len(t)):
            writer.writerow([str(t[x]), str(numvec[x]), str(numvec2[x])])
    
    #print success message
    app.addLabel("success","SUCCESS!",colspan=2)


def getsample(button):
    app.removeButton("Weigh")
    app.removeLabel("zero_w")
    tmp = float(getdata()) #"12.3752"
    app.addLabel("total_w",str(tmp)+" grams",colspan=2)
    #print "getting sample"
    app.addLabel("msg1","Press 'Start' when you are ready to collect data.",colspan=2)
    app.addLabel("msg2","Process will take 3 hours.",colspan=2)
    app.addButton("Start", gatherdata,colspan=2)
#####################################################
def start_program():
    row = app.getRow()
    app.addButton("Weigh",getsample,row,0)
    app.addLabel("zero_w","0.0000 grams",row,1)
#####################################################

#####################################################
def firstpress(button):
    global name
    global type_file
    if button =="Quit":
        app.stop
    if button=="New File":
        row=app.getRow()
        app.addLabelEntry("File Name:",row,0,colspan=2)
        app.addLabel(".csv",".csv",row,2)
        type_file=0
    #if it already exists make a drop down menu
    if button=="Old File":
        mypath=".\data\Scale"
        files=[]
        for (dirpath, dirnames, filenames) in walk(mypath):
            files.extend(filenames)
            break
        app.addLabelOptionBox("File Name",files,colspan=3)
        type_file=1
    app.removeLabel("message")
    app.removeButton("New File")
    app.removeButton("Old File")
    app.removeButton("Quit")
    app.addLabel("prompt1","Measure PLATE without and with Slurry",colspan=3)
    r=app.getRow()
    app.addNumericEntry("Plate",r,0)
    app.addNumericEntry("With",r,0)

if __name__ == '__main__':
    #initiate app
    app = gui("Scale Window","500x200")
    app.setBg("PeachPuff")
    app.setFont(12)

    #title panel
    app.addLabel("title","Scale Reading System", colspan=3)
    app.setLabelBg("title","Maroon")
    app.setLabelFg("title","PeachPuff")

    #declare Buttons
    app.addLabel("message","Does the File Already exist",colspan=3)
    app.setLabelBg("message","yellow")

    app.addButtons(["New File","Old File","Quit"],firstpress,colspan=3)
    ###### when clicked send button info to program firstpress()##### 

    app.go()
