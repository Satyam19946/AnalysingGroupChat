# # 1 - Convert your raw archived data to UTF-8 and a csv format. Can be done using notepad. file -> save as -> name.csv and change format to utf-8
Pathoffile = r"C:\Users\Satyam\Desktop\Programs\Datasets\conversation\AlphaQ"

import os
os.chdir(Pathoffile)

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 
import seaborn as sns
sns.set(style = "darkgrid")


my_data = pd.read_csv('my_data.csv')
Sender = list(my_data.Sender)
Message = list(my_data.Message)
Time = list(my_data.Time)


number = my_data.Sender.value_counts()
names = list(number.index)
number.plot.bar()
plt.title("Number of Messages Sent since 26/8/2016")
plt.show()
plt.close('all')

numbersaspercentage = [0] * len(number)
for i in range(len(number)):
	numbersaspercentage[i] = float("{0:.2f}".format((number[i]/len(Sender))*100))
plt.pie(numbersaspercentage,labels = names,autopct = '%0.2f%%')
plt.title("Percentage of Messages sent since 26/8/16")
plt.show()


begin12H = Message.index('12H') #Taking this to be  the first message sent on our group after starting 12th.
Senderbefore12 = Sender[0:begin12H]
my_databefore12 = pd.DataFrame({'Name':Senderbefore12})
numberbefore12 = my_databefore12.Name.value_counts()
namesbefore12 = list(numberbefore12.index)

Senderafter12 = Sender[begin12H:]
my_dataafter12 = pd.DataFrame({'Name':Senderafter12})
numberafter12 = my_dataafter12.Name.value_counts()
namesafter12 = list(numberafter12.index)

plt.close('all')
ax = plt.subplot()
plt.bar([0,1],[len(Senderbefore12), len(Senderafter12)])
ax.set_xticks([0,1])
ax.set_xticklabels(['Messages before 12' , 'Messages after 12'])
plt.show()

plt.close('all')
numbersaspercentage = [0] * len(numberbefore12)
for i in range(len(numberbefore12)):
	numbersaspercentage[i] = float("{0:.2f}".format(((numberbefore12[i]/begin12H))*100))
# numbersaspercentage.append(totalforlessthan1)
plt.pie(numbersaspercentage,labels = namesbefore12,autopct = '%0.2f%%')
plt.title("Percentage of Messages in 11th (Before 3/4/17)")
plt.show()



plt.close('all')
numbersaspercentage = [0] * len(numberafter12)
for i in range(len(numberafter12)):
	numbersaspercentage[i] = float("{0:.2f}".format((numberafter12[i]/len(Sender[begin12H:]))*100))
# numbersaspercentage.append(totalforlessthan1)
plt.pie(numbersaspercentage,labels = namesafter12,autopct = '%0.2f%%')
plt.title("Percentage of Messages in 12th(After 3/4/17)")
plt.show()


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

			
TotalMediaSent = listofwords.count('<Media')
			
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
words_count.head(20).plot.bar()
plt.ylabel('Number of times word sent')
plt.title('Top 20 words that are sent on this Group.')
plt.show()


Timein2400 = [0]*len(Time)
for i in range(len(Time)):
	if int(Time[i][:Time[i].index(':')]) != 12 and Time[i][-2:] != 'AM':
		Timein2400[i] += (int(Time[i][:Time[i].index(':')]) * 100) + 1200
	elif int(Time[i][:Time[i].index(':')]) != 12 or Time[i][-2:] != 'AM':
		Timein2400[i] += int(Time[i][:Time[i].index(':')]) * 100
	Timein2400[i] += int(Time[i][Time[i].index(':')+1:Time[i].index(' ')])
	
Timeheat = [0]*24
for i in range(len(Timein2400)):
	d = int(Timein2400[i]/100)
	Timeheat[d] += 1

Timelabels = ['12-1 AM', '1-2 AM' , '2-3 AM', '3-4 AM', '4-5 AM','5-6 AM','6-7 AM','7-8 AM','8-9 AM','9-10 AM','10-11 AM', '11-12 AM', '12-1 PM', '1-2 PM' , '2-3 PM', '3-4 PM' ,'4-5 PM','5-6 PM','6-7 PM','7-8 PM','8-9 PM','9-10 PM','10-11 PM','11-12 PM']

plt.close('all')
ax = plt.subplot()
Times = pd.DataFrame({'Number of Messages':Timeheat,'Time':Timelabels})
Times.plot.bar(x='Time',y='Number of Messages')
plt.title("When do we Talk the most")
plt.show()


timetakentoreply = {}
Whorepliesfast = []
for i in range(len(Sender)-1):
	if Sender[i] != Sender[i+1]:
		tt = abs(Timein2400[i]-Timein2400[i+1])
		if not (tt in timetakentoreply):
			timetakentoreply[tt] = 0
		timetakentoreply[tt] += 1
		if tt < 6:
			Whorepliesfast.append(Sender[i])
		
timetakentoreply = sorted(timetakentoreply.items(),key = lambda x:x[1])
timetakentoreply.reverse()
plt.close('all')
totaltime = 0
values = []
indexes = []
for i in range(len(timetakentoreply)):
	indexes.append(str(timetakentoreply[i][0]+1))
	values.append(timetakentoreply[i][1])
	totaltime += int(indexes[-1])*values[-1]

Averagetimetoreply = totaltime//sum(values)
ax = plt.subplot()
plt.bar(range(20),values[0:20])
ax.set_xticks(range(20))
ax.set_xticklabels(indexes[0:20])
plt.ylabel("Number of replies within x minutes -->")
plt.xlabel("Minutes -->")
plt.title("The Time waiting for replies.(Some special love towards 42)") 
plt.show()


plt.close('all')
Whorepliesfast = (pd.Series(Whorepliesfast).value_counts())
ax = plt.subplot()
plt.bar(range(len(Whorepliesfast)),Whorepliesfast)
ax.set_xticks(range(len(Whorepliesfast)))
ax.set_xticklabels(Whorepliesfast.index,rotation = 90)
plt.ylabel("Number of replies -->")
plt.title("Number of times people have replies within 5 minutes.")
plt.show()

plt.close('all')
my_data = my_data.assign(Timein2400 = Timein2400)

#Number of times people have messaged before 4 AM
NightOwls = my_data.Sender.loc[my_data.Timein2400.apply(lambda g: g <= 400)].value_counts()

#Number of times people have messaged after 4 AM but before 8 AM
EarlyBirds = my_data.Sender.loc[my_data.Timein2400.apply(lambda g: g > 400 and g < 800)].value_counts()

plt.subplot(1,2,1)
NightOwls.plot.bar()
plt.title("Night Owls (Messages sent between 12 AM and 4 AM)")

plt.subplot(1,2,2)
EarlyBirds.plot.bar()
plt.title("Early Birds (Messages sent between 4 AM and 8 AM)")

plt.show()
plt.close('all')


first = pd.DataFrame(pd.Series(Senderbefore12).value_counts())
second = pd.DataFrame(pd.Series(Senderafter12).value_counts())
total = first.join(second,lsuffix = 'first',rsuffix='second')
total = total.fillna(0)
total = total.rename(columns = {'0first':'Messages Sent in Class 11','0second':'Messages Sent in Class 12'})
total = total.assign(totals = total['Messages Sent in Class 11'] + total['Messages Sent in Class 12'])
total = total.sort_values(by = 'totals',ascending = False)
total = total.drop('totals',axis = 'columns')
sns.set()
total.plot(kind = 'bar',stacked = 'True')
plt.title("Total Messages Sent on our Group is 27594 (+-20) including " + str(TotalMediaSent)+ " Media.")
plt.show()

from wordcloud import WordCloud
text = ''
for i in listofwords:
	text += i
	text += ' '

wordcloud = WordCloud(width = 480, height = 480).generate(text)
plt.close('all')
plt.imshow(wordcloud,interpolation = 'bilinear')
plt.axis('off')
plt.margins(x = 0,y = 0)
plt.show()	
