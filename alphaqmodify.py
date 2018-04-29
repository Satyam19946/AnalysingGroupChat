#Converts a Raw Whatsapp Archived Txt into a Comma Separated ValueError

""""BEFORE RUNNING"""
#1 - Convert your raw archived data to UTF-8 and a csv format. Can be done using notepad. file -> save as -> name.csv and change format to utf-8
Pathoffile = r"C:\Users\Satyam\Desktop\Programs\Datasets\conversation\AlphaQ"

import os
os.chdir(Pathoffile)

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 
import seaborn as sns


#Reading Data and Making lists
filename = 'Alphaqv2.csv'
chat = pd.read_csv(filename)
chat = np.array(chat)
Sender = list(['']*len(chat))
Message = list(['']*len(chat))
Time = list([''] * len(chat))

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
	

my_data = pd.DataFrame({'Name':Sender})
number = my_data.Name.value_counts()
names = list(number.index)
number = list(number)
ax = plt.subplot()
plt.bar(range(len(number)),number)
ax.set_xticks(range(len(names)))
ax.set_xticklabels(names,rotation = 90)
plt.ylabel("Number of Message Sent")
plt.title("Number of Messages Sent since 26/8/2016")
# plt.show()

plt.close('all')
numbersaspercentage = [0] * len(number)
for i in range(len(number)):
	numbersaspercentage[i] = float("{0:.2f}".format((number[i]/len(Sender))*100))
# numbersaspercentage.append(totalforlessthan1)
plt.pie(numbersaspercentage,labels = names,autopct = '%0.2f%%')
plt.title("Percentage of Messages sent since 26/8/16")
# plt.show()


Senderbefore12 = Sender[0:19465]
my_databefore12 = pd.DataFrame({'Name':Senderbefore12})
numberbefore12 = my_databefore12.Name.value_counts()
namesbefore12 = list(numberbefore12.index)

Senderafter12 = Sender[19465:]
my_dataafter12 = pd.DataFrame({'Name':Senderafter12})
numberafter12 = my_dataafter12.Name.value_counts()
namesafter12 = list(numberafter12.index)

plt.close('all')
ax = plt.subplot()
plt.bar([0,1],[len(Senderbefore12), len(Senderafter12)])
ax.set_xticks([0,1])
ax.set_xticklabels(['Messages before 12' , 'Messages after 12'])
# plt.show()

plt.close('all')
numbersaspercentage = [0] * len(numberbefore12)
for i in range(len(numberbefore12)):
	numbersaspercentage[i] = float("{0:.2f}".format(((numberbefore12[i]/19465))*100))
# numbersaspercentage.append(totalforlessthan1)
plt.pie(numbersaspercentage,labels = namesbefore12,autopct = '%0.2f%%')
plt.title("Percentage of Messages Before 12 Class(4/4/17)")
# plt.show()


plt.close('all')
numbersaspercentage = [0] * len(numberafter12)
for i in range(len(numberafter12)):
	numbersaspercentage[i] = float("{0:.2f}".format((numberafter12[i]/len(Sender[19465:]))*100))
# numbersaspercentage.append(totalforlessthan1)
plt.pie(numbersaspercentage,labels = namesafter12,autopct = '%0.2f%%')
plt.title("Percentage of Messages After 12 Class(4/4/17)")
# plt.show()

listofwords = []
for i in range(len(Message)):
	msg = Message[i]
	while True:
		if ' ' in msg:
			if len(msg[:msg.index(' ')]) >= 2:
				listofwords.append(msg[:msg.index(' ')])
			msg = msg[msg.index(' ')+1:]
		else:
			if len(msg) > 2:
				listofwords.append(msg)
			break

			
def removefromlist(ls,value):
	while value in ls:
		ls.remove(value)
		
removefromlist(listofwords,'<Media')
removefromlist(listofwords,'omitted>')

arrayofwords = np.array(listofwords)
dataframeofwords = pd.DataFrame(arrayofwords)
plt.close('all')
ax = plt.subplot()
words_count = dataframeofwords[0].value_counts()
plt.bar(range(20),words_count.head(20))
ax.set_xticks(range(20))
ax.set_xticklabels(list(words_count.head(20).index))
plt.ylabel('Number of times word sent')
plt.title('Top 20 words that are sent on this Group.')
# plt.show()
