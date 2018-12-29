import datetime

def dateTime(dt):
    switcher={
            "date":datetime.date.today(),
            "time":datetime.time()
             }
    return switcher.get(dt,"invalid input")


dt=input("what do u want, date or time?: ") 
print("Today's",dt,"is",dateTime(dt))
        
   

