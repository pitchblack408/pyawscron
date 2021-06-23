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
                parts = s.split('-');
                start = int(parts[0])
                end = int(parts[1])
                for i in range(start, end + 1, 1):
                    allows.append(i)
            else:
                allows.append(int(s))
        return allows
