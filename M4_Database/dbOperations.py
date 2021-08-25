import mysql.connector


class Insert:
    def Inserting():
            
            con=mysql.connector.connect(host="localhost",user="root",password="",database="jarvis")
            cur=con.cursor()
            #query="Insert into temp4 values('{}','{}',{},'{}','{}','{}','{}','{}','{}')".format(l[0],l[1],l[2],l[3],l[4],l[5],l[6],l[7],l[8])

            d = {}
            with open("doc.txt") as f:
                while True: 
                    a = f.readline()
                    #print(a)
                    if not a:
                        break
                    else:
                        a = a.split(':-')
                        try:
                            key = a[0]
                            val = a[1].strip('\n')
                            d.update({key:val})
                        except:
                            pass
                #print(d)
            #print(d)
            l=[]
            for v in d.values():
                l.append(v)
            #print(l)
            query="Insert into temp7 values('{}','{}',{},'{}','{}','{}','{}','{}','{}')".format(l[0],l[1],l[2],l[3],l[4],l[5],l[6],l[7],l[8])
            cur.execute(query)
            con.commit()
            #x = mycol.insert_one(d)


class Retrieve:
    
    def Retrieving():
            
        con=mysql.connector.connect(host="localhost",user="root",password="",database="DoctorAssistant")
        cur=con.cursor()
            
        query = "select * from details"
        cur.execute(query)
        data=cur.fetchall()
        #print(data)
        #print(data[0][8])
        #print(data[-2])
        x=cur.rowcount
        str1=""
        if x==0:
            return "There is no data present"
        else:
            for i in data:
                #print(i)
                for j in i:
                    str1+=str(j)
                    str1+="  _  "
                str1+="\n"
        return str1

    

    


    
