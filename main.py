import requests
import json
import pandas as pd
import random
import os
from art import *

#The Jeopardy JSON file at my personal website
#Where you will find other codes and languages
url = "https://richard-perreault.com/Documents/JEOPARDY_QUESTIONS1.json"

response = requests.get(url)
data = json.loads(response.text)

global count
count = len(data)
quiz = pd.DataFrame(data)

def quizchoice():
  """Enter in a wager and get a Jeopardy question"""
  os.system('clear')
  Art=text2art("Jeopardy")
  print(Art)
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
      #This will check to see if the number is
      #an increment of 100
      wager1 = int(wager)/10
      if str(wager1).find('.0') ==-1:
        quizchoice()
        if go:
         return  
      #Make sure it is between 100 and 10000   
      if int(wager) < 100.0 or int(wager) > 10000.0:
        quizchoice()
        if go:
         return 
      if int(wager) == int(removecomma):
        go=False
      else:
        continue
    except:
      #Make sure there is no ValueError so it is just
      #numbers, and if not ask again
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