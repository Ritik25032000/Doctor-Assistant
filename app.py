from M0_Gtalk.Gtalk import gtalk as gt
from M2_VTTV.VTTV import text_voice as v
from M1_Task.Task import task as tsk
#from M4_Database.dbOperations import Insert as di, Retrieve as dr

if __name__ == "__main__":
    while True:
        query = v.takeCommand().lower()
        if  'jarvis' in query or 'hello' in query:
          gt.wishMe()
          while True:
              query = v.takeCommand().lower()
              tsk.execute(query)
              v.speak("What can I do for you")

        if 'exit' in query or 'bye' in query:
            exit()
        
        
        #if 'insert' in query:
            #di.Inserting()
            #gt.askformail()


        #if 'send' in query:
            #gt.askformail()

        