from .occurrence import Occurrence
import datetime

class AWSCron:

    MONTH_REPLACES = [
        ['JAN', '1'],
        ['FEB', '2'],
        ['MAR', '3'],
        ['APR', '4'],
        ['MAY', '5'],
        ['JUN', '6'],
        ['JUL', '7'],
        ['AUG', '8'],
        ['SEP', '9'],
        ['OCT', '10'],
        ['NOV', '11'],
        ['DEC', '12'],
    ]


    DAY_WEEK_REPLACES = [
        ['SUN', '1'],
        ['MON', '2'],
        ['TUE', '3'],
        ['WED', '4'],
        ['THU', '5'],
        ['FRI', '6'],
        ['SAT', '7'],
    ]


    def __init__(self, cron):
        self.cron = cron
        self.minutes = None
        self.hours = None
        self.days_of_month = None
        self.months = None
        self.days_of_week = None
        self.years = None
        self.rules = cron.split(' ')
        self.__parse()

    def occurrence(self, utc_datetime):
        if utc_datetime.tzinfo is None or utc_datetime.tzinfo != datetime.timezone.utc:
            raise Exception("Occurrence utc_datetime must have tzinfo == datetime.timezone.utc")
        return Occurrence(self, utc_datetime)

    def __str__(self):
        return f"cron({self.cron})"


    def __replace(self, s, rules):
        rs = str(s).upper()
        for rule in rules:
                rs = rs.replace(rule[0], rule[1])
        return rs


    def __parse(self):
        self.minutes = self.__parse_one_rule(self.rules[0], 0, 59)
        self.hours = self.__parse_one_rule(self.rules[1], 0, 23)
        self.days_of_month = self.__parse_one_rule(self.rules[2], 1, 31)
        self.months = self.__parse_one_rule(self.__replace(self.rules[3], AWSCron.MONTH_REPLACES), 1, 12)
        self.days_of_week = self.__parse_one_rule(self.__replace(self.rules[4], AWSCron.DAY_WEEK_REPLACES), 1, 7)
        self.years = self.__parse_one_rule(self.rules[5], 1970, 2199)


    def __parse_one_rule(self, rule, min, max):
        if rule == '?':
            return []
        if rule == 'L':
            return ['L', 0]
        if rule.startswith('L-'):
            return ['L', int(rule[2:])]
        if rule.endswith('L'):
            return ['L', int(rule[0:-1])]
        if rule.endswith('W'):
            return ['W', int(rule[0:-1])]
        if '#' in rule:
            return ['#', int(rule.split('#')[0]), int(rule.split('#')[1])]


        new_rule = None
        if rule == '*':
          new_rule = str(min) + "-" + str(max)
        elif '/' in rule:
            parts = rule.split('/')
            start = None
            end = None
            if parts[0] == '*':
                start = min
                end = max
            elif '-' in parts[0]:
                splits = parts[0].split('-')
                start = int(splits[0])
                end = int(splits[1])
            else:
                start = int(parts[0])
                end = max
            increment = int(parts[1])
            new_rule = ''
            while start <= end:
                new_rule += "," + str(start)
                start += increment
            new_rule = new_rule[1:]
        else:
            new_rule = rule
        allows = []
        for s in new_rule.split(','):
            if '-' in s:
                parts = s.split('-')
                start = int(parts[0])
                end = int(parts[1])
                if start <= end:
                    for i in range(start, end + 1):
                        allows.append(i)
                else:
                    for i in range(start, 8):
                        allows.append(i)
                    for i in range(1, end + 1):
                        allows.append(i)
            else:
                allows.append(int(s))
        allows.sort()
        return allows


    @staticmethod
    def get_next_n_schedule(n, from_date, cron):
        """
        Returns a list with the n next datetime(s) that match the aws cron expression from the provided start date.

        :param n: Int of the n next datetime(s)
        :param from_date: datetime with the start date
        :param cron: str of aws cron to be parsed
        :return: list of datetime objects
        """
        schedule_list = list()
        if not isinstance(from_date, datetime.datetime):
            raise ValueError("Invalid from_date. Must be of type datetime.dateime" \
                             " and have tzinfo = datetime.timezone.utc")
        else:
            cron_iterator = AWSCron(cron)
            for i in range(n):
                from_date = cron_iterator.occurrence(from_date).next()
                schedule_list.append(from_date)

            return schedule_list


    @staticmethod
    def get_prev_n_schedule(n, from_date, cron):
        """
        Returns a list with the n prev datetime(s) that match the aws cron expression 
        from the provided start date.

        :param n: Int of the n next datetime(s)
        :param from_date: datetime with the start date
        :param cron: str of aws cron to be parsed
        :return: list of datetime objects
        """
        schedule_list = list()
        if not isinstance(from_date, datetime.datetime):
            raise ValueError("Invalid from_date. Must be of type datetime.dateime" \
                             " and have tzinfo = datetime.timezone.utc")
        else:
            cron_iterator = AWSCron(cron)
            for i in range(n):
                from_date = cron_iterator.occurrence(from_date).prev()
                schedule_list.append(from_date)

            return schedule_list


    @staticmethod
    def get_all_schedule_bw_dates(from_date, to_date, cron, exclude_ends=False):
        """
        Get all datetimes from from_date to to_date matching the given cron expression.
        If the cron expression matches either 'from_date' and/or 'to_date',
        those times will be returned as well unless 'exclude_ends=True' is passed.

        :param from_date: datetime object from where the schedule will start with tzinfo in utc.
        :param to_date: datetime object to where the schedule will end with tzinfo in utc.
        :param cron: str of aws cron to be parsed
        :param exclude_ends: bool defaulted to false to not exclude the end date
        :return: list of datetime objects
        """

        if ( type(from_date) != type(to_date) and not 
            (isinstance(from_date, type(to_date)) or
            isinstance(to_date, type(from_date)))
        ):
            raise ValueError("The from_date and to_date must be same type." \
                             "  {0} != {1}".format(type(from_date), type(to_date)))
        
        elif (not isinstance(from_date, datetime.datetime) or 
            (from_date.tzinfo != datetime.timezone.utc)):
            raise ValueError("Invalid from_date and to_date. Must be of type datetime.dateime" \
                             " and have tzinfo = datetime.timezone.utc")
        else:
            schedule_list = []
            cron_iterator = AWSCron(cron)
            start = from_date.replace(second=0, microsecond=0) - datetime.timedelta(seconds=1)
            stop = to_date.replace(second=0, microsecond=0)

            while start is not None and start <= stop:
                start = cron_iterator.occurrence(start).next()
                if start is None or start > stop:
                    break
                schedule_list.append(start)

            # If exclude_ends=True , 
            # remove first & last element from the list if they match from_date & to_date
            if exclude_ends:
                if schedule_list[0] == from_date.replace(second=0,microsecond=0):
                    schedule_list.pop(0)
                if schedule_list[-1] == to_date.replace(second=0, microsecond=0):
                    schedule_list.pop()
            return schedule_list
