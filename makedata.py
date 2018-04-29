#Converts a Raw Whatsapp Group Chat Archived Txt into a Comma Separated Value

""""BEFORE RUNNING"""
#1 - Convert your raw archived data to UTF-8 and a csv format. Can be done using notepad. file -> save as -> name.csv and change format to utf-8
#Change path file accordingly
Pathoffile = r"C:\Users\Satyam\Desktop\Programs\Datasets\conversation\AlphaQ"

import os
os.chdir(Pathoffile)

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 

#Reading Data and Making lists
#Change filename accordingly
filename = 'Alphaqv2.csv'
chat = pd.read_csv(filename)
chat = np.array(chat)
Sender = list(['']*len(chat))
Message = list(['']*len(chat))

for i in range(len(chat)):
	if ':' in chat[i][0]:
		newstr = chat[i][0][chat[i][0].index(':')+1:]
	if	':' in newstr:
		Sender[i] = newstr[:newstr.index(':')]
		Message[i] = newstr[newstr.index(':')+2:]

Sender = list(filter(None, Sender))
Message = list(filter(None,Message))

for i in range(len(Sender)):
	Sender[i] = Sender[i][8:]
	
# If an error of the array Sender and Message not being same length occurs. Remove the last Sender as it is probably a repeat of the last one.
Sender.remove(Sender[-1])
	
mydata = pd.DataFrame({'Sender':Sender,'Message':Message})
mydata.to_csv('my_data.csv')
