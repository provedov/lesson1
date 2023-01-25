from datetime import datetime, date, time,timedelta
def date_in_future(arg = 0):    
    if isinstance(arg,int) == False:
        current_date = datetime.today()        
    else:
        current_date = datetime.today() + timedelta(days=arg)
    date = current_date.timetuple()
    return Print_date(date);
def Print_date(date):
    year = str(date[0])
    if date[1] < 10:
        month = '0'+str(date[1])
    else:
        month = str(date[1])
    if date[2] < 10:
        day = '0'+str(date[2])
    else:
        day = str(date[2])
    if date[3]< 10:
        hour = '0'+str(date[3])
    else:
        hour = str(date[3])
    if date[4]< 10:
        minute = '0'+str(date[4])
    else:
        minute = str(date[4])
    if date[5]< 10:
        second = '0'+str(date[5])
    else:
        second = str(date[5])
    return day+'-'+month+'-'+year+' '+hour+':'+minute+':'+second
    
