
module=[
   "Introductory Computer Networking and IT Security",
   "Software Engineering",
   "Database Design and Implementation",
   "Object Oriented Design and Programming"
     ]
time=[
   "07:00AM-09:00AM","08:00AM-10:00AM","08:00AM-11:00AM","09:00AM-10:00AM",
   "10:00AM-01:00PM","11:00AM-01:00PM","12:00PM-02:00PM","01:30PM-04:30PM"
     ]

#function  
def getRoutine(day):
     switcher={
              "sunday":   time[2]+"-->"+module[0],
              "monday":   time[1]+"-->"+module[1],
              "tuesday":  time[1]+"-->"+module[1]+"\n"+
                          time[6]+"-->"+module[3],
              "wednesday":time[0]+"-->"+module[0]+"\n"+
                          time[3]+"-->"+module[1]+"\n"+
                          time[5]+"-->"+module[2],         
              "thursday": time[4]+"-->"+module[3],
              "friday":   time[7]+"-->"+module[2],
              }
     return switcher.get(day,"invalid day")
   

#condition to loop
con=1
while(con>0):  
    day=input("enter a day? ")   
    print(getRoutine(day)+ "\n") 


     #condition to terminate 
    exit=input("do u wanna continue?[Y/N] ")
    if(exit=='y' or exit=='Y'):
        con=1
    elif(exit=='n' or exit=='N' ):
      con=0







