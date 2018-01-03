import numpy as np
from appJar import gui
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

def porosity(w1,w2,w3,d1,d2,d3):
     v_electrode=(w3-w1)*(wp_Active/p_Active+wp_Carbon/p_Carbon+wp_PVDF/p_PVDF)
     v_nmp=(w2-w3)/p_NMP
     v_procent=(d3-d1)/(d2-d1)
     return ((v_electrode+v_nmp)*(v_procent)-v_electrode)/((v_electrode+v_nmp)*v_procent)

### record samples
def get_one_sample():
     w1=float(getdata())
     d1=input("Enter distance through laser:",)
     return w1,d1

def mainthing(type):   #type=0 is new type=1 is old
     w1,w2,w3,d1,d2,d3=0,0,0,0,0,0
     #if type==1:  #old is 1
          
     #answer=raw_input("Is data for plate and beginning already stored? y/n:")
     #if answer == "n": 
     if type == 0: 
          row=app.getRow()
          app.addButton("Weigh",
          if x1 == "y":
               a=input("weigh")
               w1,d1=get_one_sample()
          x2=raw_input("Ready to collect beginning data? y/n:")
          if x2=="y":
               a=input("weigh")
               w2,d2=get_one_sample()
          with open('data/misc/'+name+'.csv', 'wb') as output:
               writer = csv.writer(output,delimiter=',')
               writer.writerow([" ","WEIGHT","DISTANCE"])
               writer.writerow(["Plate", w1, d1])
               writer.writerow(["Beginning", w2, d2])
     elif answer=="y":
          data=pd.read_csv('data/misc/'+name+'.csv')
          weightvec=data['WEIGHT'].values.tolist()
          disvec=data['DISTANCE'].values.tolist()
          w1,w2=weightvec[0],weightvec[1]
          d1,d2=disvec[0],disvec[1]               

     answer2=raw_input("Is data for the end already stored? y/n:")
     if answer2=="n":
          print('')
          x3=raw_input("Ready to collect ending data? y/n:")
          if x3=="y":
               w3,d3=get_one_sample()
               with open('data/misc/'+name+'.csv', 'wb') as output:
                    writer = csv.writer(output,delimiter=',')
                    writer.writerow([" ","WEIGHT","DISTANCE"])
                    writer.writerow(["Plate", w1, d1])
                    writer.writerow(["Beginning", w2, d2])
                    writer.writerow(["Ending", w3, d3])
          else:
               print "Thanks, Come back when drying is finished"
               sys.exit()

     elif answer2=="y":
          data=pd.read_csv('data/misc/'+name+'.csv')
          weightvec=data['WEIGHT'].values.tolist()
          disvec=data['DISTANCE'].values.tolist()
          w3=weightvec[2]
          d3=disvec[2] 

     print "Porosity:",porosity(w1,w2,w3,d1,d2,d3)
     with open('data/misc/'+name+'.csv', 'wb') as output:
          writer = csv.writer(output,delimiter=',')
          writer.writerow([" ","WEIGHT","DISTANCE"])
          writer.writerow(["Plate", w1, d1])
          writer.writerow(["Beginning", w2, d2])
          writer.writerow(["Ending", w3, d3])
          writer.writerow(["Porosity", porosity(w1,w2,w3,d1,d2,d3)])

def press(button):
     if button=="Exit":
          app.stop()
     if button=="New File":
          row=app.getRow()
          app.addLabelEntry("File Name:",row,0)
          app.addLabel(".csv",".csv",row,1)
          x=0
          mainthing(x)

     #if it already exists make a drop down menu
     if button=="Old File":
          name=app.getOptionBox("File Name")
          x=1
          mainthing(x)

if __name__=='__main__':
     #initiate app
     app=gui("Scale Window","500x200")
     app.setBg("PeachPuff")
     app.setFont(12)

     #title panel
     app.addLabel("title","Porosity System", colspan=2)
     app.setLabelBg("title","Maroon")
     app.setLabelFg("title","PeachPuff")

     #declare Buttons
     app.addLabel("message","Does the File Already exist
     app.set Bg("Blue")
     app.setFont(11)
     app.addButtons(["New File","Old File","Exit"],press,colspan2)

     mainthing()

###run gui
#def start_program():
#    row = app.getRow()
#    app.addButton("Weigh",getsample,row,0)
#    app.addLabel("zero_w","0.0000 grams",row,1)
#def press(button):
#    if button == "Exit":
#        app.stop()
#    else:
#        val = app.getEntry("File Name:")
#        #the commented out code was an experiment that worked.  I'm leaving it here for #future reference
#        #app.setLabel("message","You just started recording")
#        if val =="":
#            app.setLabel("message","Error: No filename Designated")
#            app.setLabelBg("message","red")
#if __name__ == '__main__':
#    #initiate app
#    app = gui("Scale Window","500x200")
#    app.setBg("PeachPuff")
#    app.setFont(12)
#
#    #title panel
#    app.addLabel("title","Scale Reading System", colspan=2)
#    app.setLabelBg("title","Maroon")
#    app.setLabelFg("title","PeachPuff")
#
#    #Filename input
#    row = app.getRow()
#    app.addLabelEntry("File Name:",row,0)
#    app.addLabel(".csv",".csv",row,1)
#
#    #declare buttons
#    app.addButtons(["Start Measurements","Exit"],press, colspan=2)
#
#    #message area
#    app.addLabel("message","", colspan=2)
#    #app.setLabelFg("message","Red")
#
#    app.go()
#            app.setLabelFg("message","green")
#        else:
#            app.setLabel("message","Put collector on scale and click \"weigh\" when you #have a constant value.")
#            app.setLabelBg("message","Green")
#            app.setLabelFg("message","Black")
#            app.removeButton("Start Measurements")
#            start_program()
