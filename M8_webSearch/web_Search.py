from M2_VTTV.VTTV import text_voice as v
import webbrowser

class Gsearch_python:
   def __init__(self,name_search):
      self.name = name_search
   def Gsearch(self):
      count = 0
      l=[]
      try :
         from googlesearch import search
      except ImportError:
         print("No Module named 'google' Found")
      for i in search(query=self.name,tld='co.in',lang='en',num=10,stop=5,pause=2):
         count += 1
         print (count)
         print(i + '\n')
         l.append(i)

      v.speak("Here are the results!")
      v.speak("Which number of link should I open for you?")
      t = ["first","second","third","fourth","fifth"]
      while True:
         num=v.takeCommand()
         try:
            num = int(num)
            if num > 0 and num <=5:
               webbrowser.open(l[num-1])
               break
            else:
               v.speak("You have to choose a link between 1 to 5")
         except:
            if num in t:
               webbrowser.open(l[t.index(num)])
               break
            else:
               v.speak("Sorry i did not get it can you please repeat")
            
