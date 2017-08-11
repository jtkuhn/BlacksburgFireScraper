from datetime import datetime
import calendar


def getDatetime(dateString):
    return datetime.strptime(dateString, '%m/%d/%y %H:%M')


def getWeekdayNumeric(dateString):
    datetimeObject = getDatetime(dateString)
    return datetimeObject.weekday()


def getWeekdayEnglish(dateString):
    weekday = getWeekdayNumeric(dateString)
    return calendar.day_name[weekday]