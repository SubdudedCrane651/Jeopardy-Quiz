import requests
import json
import pandas as pd
import random
import os

url = "https://richard-perreault.com/Documents/JEOPARDY_QUESTIONS1.json"

response = requests.get(url)
data = json.loads(response.text)

global count
count = len(data)
quiz = pd.DataFrame(data)

def quizchoice():
  os.system('clear')
  print("Enter from 100 to 10000 in increments of 100")
  wager =input("How much do you want to wager ")

  go=True

  while go:
    global rand
    rand = random.randrange(1,count) 
    value = quiz['value'][rand]
    #removedollar = ''.join([value for i in range(len(value)) if i != 0])
    try:
     removedollar = value
     removedollar = removedollar.replace('$', '')
     removecomma = removedollar.replace(',', '')
    except:
       removecomma=0
    
    try:
      wager1 = int(wager)/10
      if str(wager1).find('.0') ==-1:
        quizchoice()
        if go:
         return  
      if int(wager) == int(removecomma):
        go=False
      else:
        continue
    except:
      quizchoice()
      if go:
       return

quizchoice()

print("Number :"+str(rand)+"\n"
+"Category: "+quiz['category'][rand]+"\n"
+"Air Date: "+quiz['air_date'][rand]+"\n"
+"Question: "+quiz['question'][rand]+"\n"
+"Value :"+quiz['value'][rand]+"\n"
+"Round :"+quiz['round'][rand]+"\n"
+"Show number :"+quiz['show_number'][rand]+"\n")

input("<ENTER> for the Answer")
print("Answer :"+quiz['answer'][rand])