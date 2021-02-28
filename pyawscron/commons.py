import datetime
import time

class Commons:


    @staticmethod
    def python_to_aws_day_of_week(python_day_of_week):
             # MON, TUE, WED, THU, FRI, SAT, SUN
        map = {0:2, 1:3, 2:4, 3:5, 4:6, 5:7, 6:1}
        return map[python_day_of_week]

    @staticmethod
    def aws_to_python_day_of_week(aws_day_of_week):
             # MON, TUE, WED, THU, FRI, SAT, SUN
        map = {2:0, 3:1, 4:2, 5:3, 6:4, 7:5, 1:6}
        return map[aws_day_of_week]

    @staticmethod
    def array_find_first(sequence, function):
        """
        Static method
        """
        for i in sequence:
            if function(i):
                return i
        return None

    @staticmethod
    def get_days_of_month_from_days_of_week(year, month, days_of_week):
        days_of_month = []
        index = 0 # only for "#" use case
        for i in range(1, 31 + 1, 1):
            this_date = datetime.datetime(year, month, i, tzinfo=datetime.timezone.utc)
            # already after last day of month
            if this_date.month != month:
                break
            if days_of_week[0] == 'L':
                if days_of_week[1] == Commons.python_to_aws_day_of_week(this_date.weekday()) + 1:
                    same_day_next_week = datetime.datetime.fromtimestamp(int(this_date.timestamp()) + 7 * 24 * 3600, tz=datetime.timezone.utc)
                    if same_day_next_week.month != this_date.month:
                        return [i]
            elif days_of_week[0] == '#':
                if days_of_week[1] == Commons.python_to_aws_day_of_week(this_date.weekday()) + 1:
                    index += 1
                if days_of_week[2] == index:
                    return [i]
            elif Commons.python_to_aws_day_of_week(this_date.weekday()) in days_of_week:
                days_of_month.append(i)
        return days_of_month

    @staticmethod
    def get_days_of_month_for_L(year, month):
        for i in range(31,28,-1):
            this_date = datetime.datetime(year, month - 1, i, tzinfo=datetime.timezone.utc)
            if this_date.month == month - 1:
                return [i]
        raise Exception('get_days_of_month_for_L - should not happen')

    @staticmethod
    def get_days_of_month_for_W(year, month, day):
        # offset = [0, 1, -1, 2, -2].find((c) => is_weekday(year, month, day + c))
        # TODO make sure this below works
        offset = Commons.array_find_first([0, 1, -1, 2, -2], lambda c: Commons.is_weekday(year, month, day + c))
        if offset is None:
            raise Exception('get_days_of_month_for_W - should not happen')
        return [day + offset]

    @staticmethod
    def is_weekday(year, month, day):
        if day < 1 or day > 31:
            return False
        this_date =  datetime.datetime(year, month - 1, day, tzinfo=datetime.timezone.utc)
        if this_date.month != month - 1:
            return False
        return this_date.weekday() > 0 and this_date.weekday() < 6

    @staticmethod
    def current_milli_time():
        return round(time.time() * 1000)

    @staticmethod
    def datetime_to_millisec(dt_obj):
        return dt_obj.timestamp() * 1000


# const isWeekday = (year: number, month: number, day: number): boolean => {
# if (day < 1 || day > 31) {
# return false;
# }
# const thisDate = new Date(year, month - 1, day);
# if (thisDate.getMonth() !== month - 1) {
# return false;
# }
# return thisDate.getDay() > 0 && thisDate.getDay() < 6;
# };

# export const getDaysOfMonthFromDaysOfWeek = (year: number, month: number, daysOfWeek: ParsedRule) => {
# const daysOfMonth = [];
# let index = 0; // only for "#" use case
# for (let i = 1; i <= 31; i += 1) {
#     const thisDate = new Date(year, month - 1, i);
# // already after last day of month
# if (thisDate.getMonth() !== month - 1) {
# break;
# }
# if (daysOfWeek[0] === 'L') {
# if (daysOfWeek[1] === thisDate.getDay() + 1) {
# const sameDayNextWeek = new Date(thisDate.getTime() + 7 * 24 * 3600000);
# if (sameDayNextWeek.getMonth() !== thisDate.getMonth()) {
# return [i];
# }
# }
# } else if (daysOfWeek[0] === '#') {
# if (daysOfWeek[1] === thisDate.getDay() + 1) {
# index += 1;
# }
# if (daysOfWeek[2] === index) {
# return [i];
# }
# } else if (daysOfWeek.includes(thisDate.getDay() + 1)) {
# daysOfMonth.push(i);
# }
# }
# return daysOfMonth;
# };

# export const getDaysOfMonthForL = (year: number, month: number): number[] => {
# for (let i = 31; i >= 28; i -= 1) {
#     const thisDate = new Date(year, month - 1, i);
# if (thisDate.getMonth() === month - 1) {
# return [i];
# }
# }
# throw new Error('getDaysOfMonthForL - should not happen');
# };
#
# export const getDaysOfMonthForW = (year: number, month: number, day: number): number[] => {
#     const offset = [0, 1, -1, 2, -2].find((c) => isWeekday(year, month, day + c));
# if (offset === undefined) throw new Error('getDaysOfMonthForW - should not happen');
# return [day + offset];
# };

# def arrayFindFirst = (a: any[], f: any) => {
# return a.find(f);
# };

#
# export const arrayFindLast = (a: any[], f: any) => {
# // note: a.slice().reverse().find(f) is less efficient
# for (let i = a.length - 1; i >= 0; i--) {
#                                         // eslint-disable-next-line security/detect-object-injection
# const e = a[i];
# if (f(e)) {
# return e;
# }
# }
# };
