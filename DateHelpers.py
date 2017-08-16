from datetime import datetime
import calendar

dateFormats = ["%m/%d/%y %H:%M", "%m/%d/%y %I:%M%p", "%m/%d/%Y %H:%M", "%m/%d/%Y %I:%M%p", "%m-%d-%y %H:%M"]

def getDatetime(dateString):
    parseTries = 0
        
    while parseTries < len(dateFormats):
        try:
            return datetime.strptime(dateString, dateFormats[parseTries])
        except ValueError:
            pass
            
        parseTries += 1

    return None


def getWeekdayNumeric(dateString):
    datetimeObject = getDatetime(dateString)
    if datetimeObject == None:
        return None
    return datetimeObject.weekday()


def getWeekdayEnglish(dateString):
    weekday = getWeekdayNumeric(dateString)
    if weekday == None:
        return None
    return calendar.day_name[weekday]