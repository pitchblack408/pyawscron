import datetime
from dateutil.relativedelta import relativedelta

def get_days_of_month_for_L(year=2020, month=6, days_before=2):
    for i in range(31, 28 - 1, -1):
        this_date = datetime.datetime(year, month, 1, tzinfo=datetime.timezone.utc) + relativedelta(days=i-1)
        print(this_date)
        if this_date.month == month:
            return [i - days_before]
    raise Exception('get_days_of_month_for_L - should not happen')


if __name__ == '__main__':
    print(get_days_of_month_for_L())