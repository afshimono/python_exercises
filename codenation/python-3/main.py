import numpy as np
import datetime
import calendar
from calendar import monthrange

class ManagerDates:
    def date_is_valid(self, date):
        try:
            result = datetime.datetime.strptime(date, '%d/%m/%Y')
        except:
            return False
        return True

    def date_weekday(self, date):
        weekday_number = date.weekday()
        return calendar.day_name[weekday_number]

    def convert_string_to_date(self, date_str):
       
        try:
            result = datetime.datetime.strptime(date_str, '%d/%m/%Y')
        except:
            try:
                result = datetime.datetime.strptime(date_str, '%d-%m-%Y')
            except:
                try:
                    result = datetime.datetime.strptime(date_str, '%d%m%Y')
                except:
                    return False
        return result

    def get_all_dates(self, month, year):
        result = []
        _,last_day = monthrange(int(year),int(month))
        for i in np.arange(1,last_day+1):
            result.append(datetime.datetime(int(year),int(month),i))
        return result

    def count_days_mounth(self, month, year):
        first_day, last_day = monthrange(int(year),int(month))
        counter = 0
        for i in np.arange(1,last_day+1):
            if self.date_weekday(datetime.datetime(int(year),int(month),i)) not in ["Saturday","Sunday"]:
                counter += 1
        return counter

    def get_first_monday(self, year):
        i=1
        while(self.date_weekday(datetime.datetime(int(year),5,i)) != "Monday"):
            i+=1
        return datetime.datetime(int(year),5,i).strftime("%d/%m/%Y")
