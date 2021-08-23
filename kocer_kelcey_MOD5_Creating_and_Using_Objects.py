import random
import time
import os

def main():
    for i in range(3):      #Create three data files
        recordVelocity(i)
    print("All files complete!")
    
def get_MAC_address():
    listChoices = ['A','B','C','D','E','F','0','1','2','3','4','5','6','7','8','9']
    strMAC = ""
    for i in range(6):                           #Create six sets of two hexidecimal digits
        for j in range(2):
            strMAC += random.choice(listChoices) #randomly select a hexidecimal digit
        if i <5:
            strMAC += '-'                        #Seperate each group of two with a hyphen, no hyphen for the last group
    print(strMAC)
    return strMAC

def get_new_velocity(velocity):
    listChoices = [-1.0,-0.5,-0.25,-0.1,0.05,0,0,0,0,0.05,0.1,0.25,0.5,1.0] #List of possible changes in velocity
    delta = random.choice(listChoices) #randomly select a change in velocity
    new_velocity = velocity + delta    #calculate the new velocity using the original velocity and the randomly selected change
    return new_velocity

        
def recordVelocity(intFile):
    intFile += 1
    myMAC = get_MAC_address() #generates a random MAC address for UAV
    timeStart = time.time() #store the original start time
    timeNow = time.time()   #initialize the timeNow that will be updated in the loop
    delay = 0.2             #set the delay between each velocity reading
    velocity = 0.0          #initialize the velocity variable to be updated in the loop
    
    if not os.path.exists("/tmp/UNSY_329"): os.mkdir("/tmp/UNSY_329") # check for directory       
    myFile = open("/tmp/UNSY_329/3_4_Data_" + str(intFile) + ".cvs","a") # open/create the file to record the data
    
    myFile.write(myMAC + '\n')
    for i in range(0,50):
        timeNow = time.time()                           #set the time for this velocity record
        timeStamp = timeNow-timeStart                   #calculate the elapsed time
        timeStamp = "{:.5f}".format(timeStamp)          #format the time to avoid scientific notation
        myFile.write('%s,%s\n' % (timeStamp, velocity)) #write the data record to the file
        velocity = get_new_velocity(velocity)           #calculate the next velocity measurement
        time.sleep(delay)                               #wait for delay to record the next measurement
        print('File %s: %s of 50 is %s seconds @ %s m/s' % (str(intFile), i+1, timeStamp, round(velocity,3)))
    print("File " + str(intFile) +" Complete!")
    myFile.close()
main()