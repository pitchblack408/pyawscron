import math
import datetime
from datetime import tzinfo
from .commons import Commons
import time

class Occurrence():
    def __init__(self, AWSCron, utc_datetime):
        if utc_datetime.tzinfo == None or utc_datetime.tzinfo != datetime.timezone.utc:
            raise Exception("Occurance utc_datetime must have tzinfo == datetime.timezone.utc")
        self.utc_datetime = utc_datetime
        self.cron = AWSCron
        self.iter = 0



    def __find_once(self, parsed, datetime_from):

        if self.iter > 10:
            raise Exception("AwsCronParser : this shouldn't happen, but iter > 10")
        self.iter += 1
        current_year = datetime_from.year
        current_month = datetime_from.month
        current_day_of_month = datetime_from.day
        current_hour = datetime_from.hour
        current_minute = datetime_from.minute
        year = Commons.array_find_first(parsed.years, lambda c: c >= current_year)
        if year is None:
            return None
        month = Commons.array_find_first(parsed.months, lambda c: c >= ( current_month if year == current_year else 1))
        if not month:
            return self.__find_once(parsed, datetime.datetime(year + 1, 0, tzinfo=datetime.timezone.utc))
        is_same_month = True if year == current_year and month == current_month else False
        p_days_of_month = parsed.days_of_month
        if len(p_days_of_month) == 0:
            p_days_of_month = Commons.get_days_of_month_from_days_of_week(year, month, parsed.daysOfWeek)
        elif p_days_of_month[0] == 'L':
            p_days_of_month = Commons.get_days_of_month_for_L(year, month)
        elif p_days_of_month[0] == 'W':
            p_days_of_month = Commons.get_days_of_month_for_W(year, month, p_days_of_month[1])
        day_of_month = Commons.array_find_first(p_days_of_month, lambda c:  c >= ( current_day_of_month if is_same_month else 1))
        if not day_of_month:
            return self.__find_once(parsed, datetime.datetime(year, month + 1, 1, tzinfo=datetime.timezone.utc))
        is_same_date = is_same_month and day_of_month == current_day_of_month
        hour = Commons.array_find_first(parsed.hours, lambda c:  c >= (current_hour if is_same_date else 0))
        if hour is None:
            return self.__find_once(parsed, datetime.datetime(year, month, day_of_month + 1, tzinfo=datetime.timezone.utc))
        minute = Commons.array_find_first(parsed.minutes, lambda c: c >= (current_minute if is_same_date and hour == current_hour else 0))
        if minute == None:
            return self.__find_once(parsed, datetime.datetime(year, month, day_of_month, hour + 1, tzinfo=datetime.timezone.utc))

        return datetime.datetime(year, month, day_of_month, hour, minute, tzinfo=datetime.timezone.utc)


    def next(self):
        self.iter = 0
        from_epoch = (math.floor(Commons.datetime_to_millisec(self.utc_datetime)/60000.0) + 1) * 60000
        dt = datetime.datetime.fromtimestamp(from_epoch / 1000.0, tz=datetime.timezone.utc)
        return self.__find_once(self.cron, dt)