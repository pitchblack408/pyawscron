**Main Branch Status**

![](https://github.com/pitchblack408/pyawscron/actions/workflows/python-pyawscron.yml/badge.svg?branch=main)

**Develop Branch Status**

![](https://github.com/pitchblack408/pyawscron/actions/workflows/python-pyawscron.yml/badge.svg?branch=develop)




# pyawscron

A python port from a typescript project.

https://github.com/beemhq/aws-cron-parser

# Install
    pip install pyawscron

## [AWS Cron Expressions](https://docs.aws.amazon.com/AmazonCloudWatch/latest/events/ScheduledEvents.html#CronExpressions)
### cron(fields)
<table>
   <thead>
      <tr>
         <th><b>Field</b></th>
         <th><b>Values</b></th>
         <th><b>Wildcards</b></th>
      </tr>
   </thead>
   <tbody>
      <tr>
         <td>
            <p>Minutes</p>
         </td>
         <td>
            <p>0-59</p>
         </td>
         <td>
            <p>, - * /</p>
         </td>
      </tr>
      <tr>
         <td>
            <p>Hours</p>
         </td>
         <td>
            <p>0-23</p>
         </td>
         <td>
            <p>, - * /</p>
         </td>
      </tr>
      <tr>
         <td>
            <p>Day-of-month</p>
         </td>
         <td>
            <p>1-31</p>
         </td>
         <td>
            <p>, - * ? / L W</p>
         </td>
      </tr>
      <tr>
         <td>
            <p>Month</p>
         </td>
         <td>
            <p>1-12 or JAN-DEC</p>
         </td>
         <td>
            <p>, - * /</p>
         </td>
      </tr>
      <tr>
         <td>
            <p>Day-of-week</p>
         </td>
         <td>
            <p>1-7 or SUN-SAT</p>
         </td>
         <td>
            <p>, - * ? L #</p>
         </td>
      </tr>
      <tr>
         <td>
            <p>Year</p>
         </td>
         <td>
            <p>1970-2199</p>
         </td>
         <td>
            <p>, - * /</p>
         </td>
      </tr>
   </tbody>
</table>

### Wildcards
* The , (comma) wildcard includes additional values. In the Month field, JAN,FEB,MAR would include January, February, and March.
* The - (dash) wildcard specifies ranges. In the Day field, 1-15 would include days 1 through 15 of the specified month.
* The * (asterisk) wildcard includes all values in the field. In the Hours field, * would include every hour. You cannot use * in both the Day-of-month and Day-of-week fields. If you use it in one, you must use ? in the other.
* The / (forward slash) wildcard specifies increments. In the Minutes field, you could enter 1/10 to specify every tenth minute, starting from the first minute of the hour (for example, the 11th, 21st, and 31st minute, and so on).
* The ? (question mark) wildcard specifies one or another. In the Day-of-month field you could enter 7 and if you didn't care what day of the week the 7th was, you could enter ? in the Day-of-week field.
* The L wildcard in the Day-of-month or Day-of-week fields specifies the last day of the month or week.
* The W wildcard in the Day-of-month field specifies a weekday. In the Day-of-month field, 3W specifies the weekday closest to the third day of the month.
* The # wildcard in the Day-of-week field specifies a certain instance of the specified day of the week within a month. For example, 3#2 would be the second Tuesday of the month: the 3 refers to Tuesday because it is the third day of each week, and the 2 refers to the second day of that type within the month.



# Iterative Use

**next**

    from pyawscron import AWSCron
    import datetime
    import calendar
    
    def main():
    
        aws_cron = AWSCron("0 5 4 * ? *")
        today = datetime.datetime.utcnow().date()
        start_date = datetime.datetime(today.year, today.month, 1, tzinfo=datetime.timezone.utc)
        last_day = calendar.monthrange(today.year, today.month)[1]
        end_date = datetime.datetime(today.year, today.month, last_day, tzinfo=datetime.timezone.utc)
        dt=start_date
        while True:
            dt = aws_cron.occurrence(dt).next()
            if dt > end_date:
                break
            print(dt)
    
    
    if __name__ == "__main__":
        main()
    
**prev**

    from pyawscron import AWSCron
    import datetime
    
    def main():
    
        aws_cron = AWSCron("0 5 4 * ? *")
        today = datetime.datetime.utcnow().date()
        start_date = datetime.datetime(today.year, today.month, 1, tzinfo=datetime.timezone.utc)
        end_date = datetime.datetime(today.year, today.month-1, 1, tzinfo=datetime.timezone.utc)
        dt=start_date
        while True:
            dt = aws_cron.occurrence(dt).prev()
            if dt < end_date:
                break
            print(dt)
    
    
    if __name__ == "__main__":
        main()

## Helper Methods
### get_all_schedule_bw_dates
Returns a list of UTC datetime objects using a start and end date. The end date has a flag to be inclusive or exclusive.

**Note:** This method has no limit on how many datetime object can be returned. Use Iterative approach or get_next_n_schedule if memory becomes an issue.

```
from_dt = datetime.datetime(2021, 8, 7, 8, 30, 57, tzinfo=datetime.timezone.utc)
to_date = datetime.datetime(2021, 8, 7, 11, 30, 57, tzinfo=datetime.timezone.utc)

AWSCron.get_all_schedule_bw_dates(from_dt, to_date, '0/23 * * * ? *')

# Resulting list
[datetime.datetime(2021, 8, 7, 8, 46, tzinfo=datetime.timezone.utc),
datetime.datetime(2021, 8, 7, 9, 0, tzinfo=datetime.timezone.utc),
datetime.datetime(2021, 8, 7, 9, 23, tzinfo=datetime.timezone.utc),
datetime.datetime(2021, 8, 7, 9, 46, tzinfo=datetime.timezone.utc),
datetime.datetime(2021, 8, 7, 10, 0, tzinfo=datetime.timezone.utc),
datetime.datetime(2021, 8, 7, 10, 23, tzinfo=datetime.timezone.utc),
datetime.datetime(2021, 8, 7, 10, 46, tzinfo=datetime.timezone.utc),
datetime.datetime(2021, 8, 7, 11, 0, tzinfo=datetime.timezone.utc),
datetime.datetime(2021, 8, 7, 11, 23, tzinfo=datetime.timezone.utc)]
```
### get_next_n_schedule
Returns a list with the n next datetimes that match the aws cron expression from the provided start date.

```
from_dt = datetime.datetime(2021, 8, 7, 8, 30, 57, tzinfo=datetime.timezone.utc)

AWSCron.get_next_n_schedule(10, from_dt, '0/23 * * * ? *')

# Resulting list
[datetime.datetime(2021, 8, 7, 8, 46, tzinfo=datetime.timezone.utc),
datetime.datetime(2021, 8, 7, 9, 0, tzinfo=datetime.timezone.utc),
datetime.datetime(2021, 8, 7, 9, 23, tzinfo=datetime.timezone.utc),
datetime.datetime(2021, 8, 7, 9, 46, tzinfo=datetime.timezone.utc),
datetime.datetime(2021, 8, 7, 10, 0, tzinfo=datetime.timezone.utc),
datetime.datetime(2021, 8, 7, 10, 23, tzinfo=datetime.timezone.utc),
datetime.datetime(2021, 8, 7, 10, 46, tzinfo=datetime.timezone.utc),
datetime.datetime(2021, 8, 7, 11, 0, tzinfo=datetime.timezone.utc),
datetime.datetime(2021, 8, 7, 11, 23, tzinfo=datetime.timezone.utc),
datetime.datetime(2021, 8, 7, 11, 46, tzinfo=datetime.timezone.utc)]
```
### get_prev_n_schedule
Returns a list with the n prev datetimes that match the aws cron expression from the provided start date.

```
from_dt = datetime.datetime(2021, 8, 7, 11, 50, 57, tzinfo=datetime.timezone.utc)

AWSCron.get_prev_n_schedule(10, from_dt, '0/23 * * * ? *')

# Resulting list
[datetime.datetime(2021, 8, 7, 11, 46, tzinfo=datetime.timezone.utc),
 datetime.datetime(2021, 8, 7, 11, 23, tzinfo=datetime.timezone.utc),
 datetime.datetime(2021, 8, 7, 11, 0, tzinfo=datetime.timezone.utc),
 datetime.datetime(2021, 8, 7, 10, 46, tzinfo=datetime.timezone.utc),
 datetime.datetime(2021, 8, 7, 10, 23, tzinfo=datetime.timezone.utc),
 datetime.datetime(2021, 8, 7, 10, 0, tzinfo=datetime.timezone.utc),
 datetime.datetime(2021, 8, 7, 9, 46, tzinfo=datetime.timezone.utc),
 datetime.datetime(2021, 8, 7, 9, 23, tzinfo=datetime.timezone.utc),
 datetime.datetime(2021, 8, 7, 9, 0, tzinfo=datetime.timezone.utc),
 datetime.datetime(2021, 8, 7, 8, 46, tzinfo=datetime.timezone.utc)]
```


