#Converts a Raw Whatsapp Group Chat Archived Txt into a Comma Separated ValueError

""""BEFORE RUNNING"""
#1 - Convert your raw archived data to UTF-8 and a csv format. Can be done using notepad. file -> save as -> name.csv and change format to utf-8
#2 - Open the file in excel and delete the entire column of Dates and shift the cells to the left. This is necessary because Whatsapp messages
     #containg enter (new lines) are taken as new entries and thus the read_csv() function is not able to read them.
#Change path file accordingly
Pathoffile = r"C:\Users\Satyam\Desktop\Programs\Datasets\conversation\AlphaQ"

import os
os.chdir(Pathoffile)

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 
import time

#Reading Data and Making lists
#Change filename accordingly
filename = 'Alphaq.csv'
chat = pd.read_csv(filename)
chat = np.array(chat)
Sender = list(['']*len(chat))
Message = list(['']*len(chat))
Time = list(([''])*len(chat))

for i in range(len(chat)):
	if ':' in chat[i][0]:  #This removes notifs like 'X' added 'y' in group.
		newstr = chat[i][0][chat[i][0].index(':')+1:]
	if ':' in newstr and 'M' in chat[i][0]:  #This removes notifs like 'X' changed the groups name, icon, left the group etc.
		Time[i] = chat[i][0][1:chat[i][0].index('M')+1]
		Sender[i] = newstr[:newstr.index(':')]
		Message[i] = newstr[newstr.index(':')+2:]

#Remove no Senders errors, newlines from messages, and entries with no Time.
Sender = list(filter(None, Sender))
Message = list(filter(None,Message))
Time = list(filter(None,Time))

for i in range(len(Sender)):
	Sender[i] = Sender[i][8:]
	

Sender.remove(Sender[-1])
Time.remove(Time[-1])
mydata = pd.DataFrame({'Time':Time, 'Sender':Sender,'Message':Message})
# mydata.to_csv('my_data.csv')
