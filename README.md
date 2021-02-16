# pyawscron

A python port from a typescript project.
https://github.com/beemhq/aws-cron-parser


There is only one method implemented:

    cron = '23,24,25 17,18 25 MAR/4 ? 2020,2021,2023,2028'
    cron = AWSCron(cron)
    dt = datetime.datetime(2020, 5, 9, 22, 30, 57, tzinfo=datetime.timezone.utc)
    dt = cron.occurance(dt).next()
 
 Result
 
    '2020-07-25 17:23:00+00:00',
    
    
    
    