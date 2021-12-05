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
  print("[1] 100 [2] 200 [3] 300 [4] 400 [5] 500 [6] 600 [7] 800 [8] 1000 [9] 1200 [10] 1600 [11] 2000")
  wager =input("How much do you want to wager ")

  go=True

  while go:
    global rand
    rand = random.randrange(1,count+1) 
    value = quiz['value'][rand]
    #removedollar = ''.join([value for i in range(len(value)) if i != 0])
    removedollar = value
    removedollar = removedollar.replace('$', '')
    try:
     removecomma = removedollar.replace(',', '')
    except:
       removecomma=removedollar
    
    if wager == '1':    
      if int(removecomma) == 100:
        go=False
      else:
        go=True
    elif wager == '2':
      if int(removecomma) == 200:
        return
      else:
        go=True
    elif wager == '3':
      if int(removecomma) == 300:
        go=False
      else:
        go=True
    elif wager == '4':
      if int(removecomma) == 400:
        go=False
      else:
        go=True
    elif wager == '5':
      if int(removecomma) == 500:
       go=False
      else:
        go=True
    elif wager == '6':
     if int(removecomma) == 600:
        go=False
     else:
        go=True      
    elif wager == '7':
      if int(removecomma) == 800:
        go=False
      else:
        go=True
    elif wager == '8':
      if int(removecomma) == 1000:
        go=False
      else:
        go=True 
    elif wager == '9':
      if int(removecomma) == 1200:
        go=False
      else:
        go=True
    elif wager == '10':
      if int(removecomma) == 1600:
        go=False
      else:
        go=True
    elif wager == '11':
      if int(removecomma) == 2000:
        go=False
      else:
        go=True
    elif wager == '':
      quizchoice()
   

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