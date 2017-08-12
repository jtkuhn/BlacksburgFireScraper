from datetime import datetime
import calendar

dateFormats = ["%m/%d/%y %H:%M", "%m/%d/%y %I:%M%p", "%m/%d/%Y %H:%M", "%m/%d/%Y %I:%M%p", "%m-%d-%y %H:%M"]

def getDatetime(dateString):
    returnValue = None
    parseTries = 0
        
    while returnValue == None and parseTries < len(dateFormats):
        try:
            returnValue = datetime.strptime(dateString, dateFormats[parseTries])
        except ValueError:
            pass
            
        parseTries += 1

    return returnValue


def getWeekdayNumeric(dateString):
    datetimeObject = getDatetime(dateString)
    return datetimeObject.weekday()


def getWeekdayEnglish(dateString):
    weekday = getWeekdayNumeric(dateString)
    return calendar.day_name[weekday]