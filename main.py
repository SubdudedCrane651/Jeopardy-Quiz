import requests
import json
import pandas as pd
import random

url = "https://richard-perreault.com/Documents/JEOPARDY_QUESTIONS1.json"

response = requests.get(url)
data = json.loads(response.text)

count = len(data)
quiz = pd.DataFrame(data)

print("[1] 100 [2] 200 [3] 400 [4] 500 [5] 600 [6] 700 [7] 800 [8] 1000 [9] 1200")
wager =input("How much do you want to wager ")

go=True 

while go:
 rand = random.randrange(1,count) 
 value = quiz['value'][rand]
 #removedollar = ''.join([value for i in range(len(value)) if i != 0])
 removedollar =  value.replace('$', '')
 removecomma =  removedollar.replace(',', '')
 try:
  if int(wager) == 1:    
    if int(removecomma) == 100:
      go = False
  elif int(wager) == 2:
    if int(removecomma) == 200:
      go = False
  elif int(wager) == 3:
    if int(removecomma) == 400:
      go = False
  elif int(wager) == 4:
    if int(removecomma) == 500:
      go = False
  elif int(wager) == 5:
    if int(removecomma) == 600:
      go = False
  elif int(wager) == 6:
    if int(removecomma) == 700:
      go = False      
  elif int(wager) == 7:
    if int(removecomma) == 800:
      go = False
  elif int(wager) == 8:
    if int(removecomma) == 1000:
      go = False 
  elif int(wager) == 9:
    if int(removecomma) == 1200:
      go = False
  elif int(wager) == 10:
    if int(removecomma) == 1400:
      go = False
 except:
  go=Tue            :
                 

print("Number :"+str(rand)+"\n"
+"Category: "+quiz['category'][rand]+"\n"
+"Air Date: "+quiz['air_date'][rand]+"\n"
+"Question: "+quiz['question'][rand]+"\n"
+"Value :"+quiz['value'][rand]+"\n"
+"Round :"+quiz['round'][rand]+"\n"
+"Show number :"+quiz['show_number'][rand]+"\n")

input("<ENTER> for the Answer")
print("Answer :"+quiz['answer'][rand])