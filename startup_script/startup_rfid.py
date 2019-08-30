from os.path import expanduser
import datetime
import time
import os
import subprocess #maybe this would be useful for starting BRMSample
import pynput #keypress library
from pynput.keyboard import Key, Controller

#This is the startup script for the RFID module


#1. check rest api first (getstatus), implement here




#2. start RFID module
sudoPassword = 'Radiohead'
command = 'gnome-terminal -x sudo /home/veera/radiohead-master/BRMSample/build/release/BRMSample'
p = os.system('echo %s|sudo -S %s' % (sudoPassword, command))

#wait a bit
time.sleep(2)


keyboard=Controller()
keyboard.press(Key.tab)
keyboard.release(Key.tab)
#keyboard press s is for starting the reading, d is for stop command and writing the csv file
i=0
while i<10:
	keyboard.press('s')
	keyboard.release('s')
	time.sleep(1)
	i+=1




#3. hex2decimal conversion after stop command, implement here


#4. mysql combination of rfid data and restapi coordinates after hex2decimal conversion


#this is some random stuff
#os.system('gnome-terminal -x sudo /home/jonathan/BRMSample/build/release/BRMSample')
