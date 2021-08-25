import datetime
import sys  
#sys.path.append('C:\Project Git Hub\Jarvis_Assistant\Jarvis')
from M2_VTTV.VTTV import text_voice as v
from M3_Pwriter.fwrite import file_op as fop
from M3_Pwriter.formatter import format as fw, dr_detail as dd
from M7_editor.texteditor import*
from M8_webSearch.web_Search import Gsearch_python as gp
from M4_Database.dbOperations import Insert as di, Retrieve as dr
#,Database_update as up,Database_delete as de
from M0_Gtalk.Gtalk import gtalk as gt
#from M10_csvfile.tocsv import tocsvfile as t


class task:
    def execute(query):
        if 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            v.speak(f"Sir, the time is {strTime}")
            
        elif 'patient' in query:
            content=fw.set_format()
            fop.write_text(content)
            editor()
            di.Inserting()
            #t.export()
            gt.askformail()
            
        elif 'my profile' in query:
            detail=dd.set_detail()
            fop.write_detail(detail)
            editor2()

        elif 'search' in query:
            v.speak("What can I search for you.")
            a = gp(v.takeCommand())
            a.Gsearch()
            
        elif 'exit' in query:
            exit()
            
        elif 'retrieve' in query:
            str1=dr.Retrieving()
            print(str1)
                
                    
        else:
            v.speak("Sorry! I didn't get anything.")
            return
        '''
        elif 'update' in query or 'change' in query:
            while True:
                up.update(dr)
                v.speak("Do you again want to update!")
                str= v.takeCommand().lower()
                if 'yes' in str or 'None' in str:
                    pass
                else:
                    break
            t.export()

        elif 'delete' in query or 'remove' in query:
            while True:
                de.delete()
                v.speak("Do you again want to delete!")
                str= v.takeCommand().lower()
                if 'yes' in str or 'None' in str:
                    pass
                else:
                    break
            t.export()
        '''
        
            
        v.speak("The work has been done successfully. I hope you are satisfied with the results!")
        v.speak("Do you want to continue")
        str = v.takeCommand().lower()
        if 'y' in str or 'ok' in str:
            pass
        elif 'pause' in str or 'wait' in str or 'jarvis' in str:
            v.speak("Ok doctor i am waiting")
            str = input()
        else:
            exit()