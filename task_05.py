from datetime import datetime, date, time,timedelta
def date_in_future(arg):    
    if isinstance(arg,int) == False:
        current_date = datetime.today()        
    else:
        current_date = datetime.today() + timedelta(days=arg)
    date = current_date.timetuple()
    Print_date(date);
def Print_date(date):
    year = date[0]
    month = date[1]
    day = date[2]
    hour = date[3]
    minute = date[4]
    second = date[5]
    print(str(day)+'-'+str(month)+'-'+str(year)+' '+str(hour)+':'+str(minute)+':'+str(second))
    
