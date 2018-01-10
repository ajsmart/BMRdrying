import numpy as np
from appJar import gui
from os import walk
from readScale import getdata
from readScale import close
from readScale import take_measurements
import csv
import sys
import pandas as pd

wp_Active=.92
wp_Carbon=.04
wp_PVDF=.04
p_Active=4.9  #g/cm3
p_Carbon=1.9  #g/cm3
p_PVDF=1.78   #g/cm3
p_NMP=1.03    #g/cm3

######## Declare GLOBAL variables
w1,w2,w3,d1,d2,d3=1,1,1,1,1,1
name=""
type=0
#################

def porosity():
     global w1,w2,w3,d1,d2,d3
     if d2==d1:
          app.addLabel("error","ERROR DEVIDE BY ZERO",colspan=3)
     v_electrode=(w3-w1)*(wp_Active/p_Active+wp_Carbon/p_Carbon+wp_PVDF/p_PVDF)
     v_nmp=(w2-w3)/p_NMP
     v_procent=(d3-d1)/(d2-d1)
     return ((v_electrode+v_nmp)*(v_procent)-v_electrode)/((v_electrode+v_nmp)*v_procent)

######## Read File Doesn't work
def readfile():
     global w1,w2,w3,d1,d2,d3
     global name
     data=pd.read_csv('data/por/'+name+'.csv')
     weightvec=data['WEIGHT'].values.tolist()
     disvec=data['DISTANCE'].values.tolist()
     w1,w2,w3=weightvec[0],weightvec[1],weightvec[2]
     d1,d2,d3=disvec[0],disvec[1],disvec[2]

def writefile():
     global w1,w2,w3,d1,d2,d3
     global name
     d1=app.getEntry("Plate:")
     d2=app.getEntry("Beginning:")
     d3=app.getEntry("Ending:")
     
     with open('data/por/'+name+'.csv', 'wb') as output:
          writer = csv.writer(output,delimiter=',')
          writer.writerow([" ","WEIGHT","DISTANCE"])
          writer.writerow(["Plate", w1, d1])
          writer.writerow(["Beginning", w2, d2])
          writer.writerow(["Ending", w3, d3])
          writer.writerow(["Porosity",porosity()])

def mainthing(button):
     global w1,w2,w3,d1,d2,d3
     global type
     global name
     if type == 0:
          name=app.getEntry("File Name:")
     if type == 1:
          x=1
          #readfile()
     if button == "Plate":
          w1= float(getdata())
          #get data for plate   
     if button == "Beginning":
          w2= float(getdata())
          #get data for beginning
     if button == "Ending":
          #get data for ending 
          w3= float(getdata())
     if button=="Porosity":
          por="Porosity: "+str(porosity())
          app.addLabel("output",por,colspan=3)
          
     if button=="Save & Quit":
          writefile()
          app.stop()
     return

def press(button):
     global type
     if button=="New File":
          global type
          row=app.getRow()
          #app.addLabelEntry("File Name:",row,0)
          app.addLabelEntry("File Name:",row,0,colspan=3)
          app.addLabel(".csv",".csv",row,2)
          type=0

     #if it already exists make a drop down menu
     if button=="Old File":
          global name
          global type
          mypath=".\data\por"
          files=[]
          for (dirpath, dirnames, filenames) in walk(mypath):
               files.extend(filenames)
               break
          name=app.addLabelOptionBox("File Name",files)
          type=1

     app.removeLabel("message")
     app.removeButton("New File")
     app.removeButton("Old File")
     app.addLabel("message1","Weigh Electrode",colspan=3)
     app.setLabelBg("message1","yellow")
     app.addButtons(["Plate","Beginning","Ending"],mainthing,colspan=3)

     app.addLabel("message2","Measure distance",colspan=3)
     app.setLabelBg("message2","yellow")
     rowd=app.getRow()
     name=app.addLabelEntry("Plate:",rowd,0)
     name=app.addLabelEntry("Beginning:",rowd,1)
     name=app.addLabelEntry("Ending:",rowd,2)

     app.addButtons(["Porosity","Save & Quit"],mainthing,colspan=3)

if __name__=='__main__':
     #initiate app
     app=gui("Scale Window","500x300")
     app.setBg("PeachPuff")
     app.setFont(12)

     #title panel
     app.addLabel("title","Porosity System",colspan=3)
     app.setLabelBg("title","Maroon")
     app.setLabelFg("title","PeachPuff")

     #declare Buttons
     app.addLabel("message","Does the File Already exist",colspan=3)
     app.setLabelBg("message","yellow")

     app.addButtons(["New File","Old File"],press,colspan=3)
     ###### when clicked send button info to program press()##### 
     
     app.go()

