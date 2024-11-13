
# -*- coding: utf-8 -*-

import unittest
import datetime
from src.pyawscron import AWSCron

class NextTestCase(unittest.TestCase):


    def setUp(self):
        print(self._testMethodName)


    def tearDown(self):
        pass

    def test_generate_multiple_next_occurences1(self):
        """At 23, 24, and 25 minutes past the hour, at 05:00 PM and 06:00 PM,
           on day 25 of the month, every 4 months, March through December,
           only in 2020, 2021, 2023, and 2028
           cron(Minutes Hours Day-of-month Month Day-of-week Year)
           / ==>> This character is used to specify increments.
        :return:
        """
        cron = '23,24,25 17,18 25 MAR/4 ? 2020,2021,2023,2028'
        expected_list= ['2020-07-25 17:23:00+00:00',
                        '2020-07-25 17:24:00+00:00',
                        '2020-07-25 17:25:00+00:00',
                        '2020-07-25 18:23:00+00:00',
                        '2020-07-25 18:24:00+00:00',
                        '2020-07-25 18:25:00+00:00',

                        '2020-11-25 17:23:00+00:00',
                        '2020-11-25 17:24:00+00:00',
                        '2020-11-25 17:25:00+00:00',
                        '2020-11-25 18:23:00+00:00'
                        ]
        cron = AWSCron(cron)
        dt = datetime.datetime(2020, 5, 9, 22, 30, 57, tzinfo=datetime.timezone.utc)
        results = []
        for expected in expected_list:
            print(f"Input {cron}, occurrence: {dt}")
            dt = cron.occurrence(dt).next()
            results.append(str(dt))
            print(f"Result: {dt}\tExpected: {expected}\n")
            self.assertEqual(expected, str(dt))



    def test_generate_multiple_next_occurences2(self):
        """At 10:15 AM, on the last Friday of the month, 2002 through 2025
           cron(Minutes Hours Day-of-month Month Day-of-week Year)
           L ==>> This character is used to specify last day of the month or week
        :return:
        """
        cron = '15 10 ? * 6L 2002-2025'
        expected_list = ['2020-05-29 10:15:00+00:00',
                         '2020-06-26 10:15:00+00:00',
                         '2020-07-31 10:15:00+00:00',
                         '2020-08-28 10:15:00+00:00',
                         '2020-09-25 10:15:00+00:00',
                         '2020-10-30 10:15:00+00:00',
                         '2020-11-27 10:15:00+00:00',
                         '2020-12-25 10:15:00+00:00',
                         '2021-01-29 10:15:00+00:00',
                         '2021-02-26 10:15:00+00:00'
                         ]

        cron = AWSCron(cron)
        dt = datetime.datetime(2020, 5, 9, 22, 30, 57, tzinfo=datetime.timezone.utc)
        results = []
        for expected in expected_list:
            print(f"Input {cron}, occurrence: {dt}")
            dt = cron.occurrence(dt).next()
            results.append(str(dt))
            print(f"Result: {dt}\tExpected: {expected}\n")
            self.assertEqual(expected, str(dt))

    def test_generate_multiple_next_occurences3(self):
        """Every 3 hours
           cron(Minutes Hours Day-of-month Month Day-of-week Year)
        :return:
        """
        cron = '0 */3 */1 * ? *'
        expected_list = ['2020-12-07 18:00:00+00:00',
                         '2020-12-07 21:00:00+00:00',
                         '2020-12-08 00:00:00+00:00',
                         '2020-12-08 03:00:00+00:00'
                         ]
        cron = AWSCron(cron)
        dt = datetime.datetime(2020, 12, 7, 15, 57, 37, tzinfo=datetime.timezone.utc)
        results = []
        for expected in expected_list:
            print(f"Input {cron}, occurrence: {dt}")
            dt = cron.occurrence(dt).next()
            results.append(str(dt))
            print(f"Result: {dt}\tExpected: {expected}\n")
            self.assertEqual(expected, str(dt))

    def test_generate_multiple_next_occurences4(self):
        """At 12:15 PM, only on Sunday and Monday
           cron(Minutes Hours Day-of-month Month Day-of-week Year)
        :return:
        """
        cron = '15 12 ? * sun,mon *'
        expected_list = ['2020-12-13 12:15:00+00:00',
                         '2020-12-14 12:15:00+00:00',
                         '2020-12-20 12:15:00+00:00',
                         '2020-12-21 12:15:00+00:00'
                         ]
        cron = AWSCron(cron)
        dt = datetime.datetime(2020, 12, 7, 15, 57, 37, tzinfo=datetime.timezone.utc)
        results = []
        for expected in expected_list:
            print(f"Input {cron}, occurrence: {dt}")
            dt = cron.occurrence(dt).next()
            results.append(str(dt))
            print(f"Result: {dt}\tExpected: {expected}\n")
            self.assertEqual(expected, str(dt))

    def test_generate_multiple_next_6(self):
        """At 10 minutes past the hour, every 5 hours, starting at 07:00 AM, on day 7 of the month,
           only in 2020 and 2021
           cron(Minutes Hours Day-of-month Month Day-of-week Year)
           / ==>> This character is used to specify increments.
        :return:
        """
        cron = '10 7/5 7 * ? 2020,2021'
        expected_list = ['2020-12-07 17:10:00+00:00',
                         '2020-12-07 22:10:00+00:00',
                         '2021-01-07 07:10:00+00:00',
                         '2021-01-07 12:10:00+00:00'
                         ]
        cron = AWSCron(cron)
        dt = datetime.datetime(2020, 12, 7, 15, 57, 37, tzinfo=datetime.timezone.utc)
        results = []
        for expected in expected_list:
            print(f"Input {cron}, occurrence: {dt}")
            dt = cron.occurrence(dt).next()
            results.append(str(dt))
            print(f"Result: {dt}\tExpected: {expected}\n")
            self.assertEqual(expected, str(dt))


# Good test for parsing as well
    def test_generate_multiple_next_7(self):
        """Every minute between 10:00 PM and 10:/5 PM, on day 09 of the month, only in May,
           only in 2020, 2021, and 2022
           cron(Minutes Hours Day-of-month Month Day-of-week Year)
           / ==>> This character is used to specify increments.
           - ==>> This character is used to specifies ranges.
        :return:
        """
        cron = '0-29/5 22 09 05 ? 2020,2021,2022'
        expected_list = ['2021-05-09 22:00:00+00:00',
                         '2021-05-09 22:05:00+00:00',
                         '2021-05-09 22:10:00+00:00',
                         '2021-05-09 22:15:00+00:00',
                         '2021-05-09 22:20:00+00:00',
                         '2021-05-09 22:25:00+00:00',
                         '2022-05-09 22:00:00+00:00',
                         '2022-05-09 22:05:00+00:00',
                         '2022-05-09 22:10:00+00:00',
                         '2022-05-09 22:15:00+00:00',
                         '2022-05-09 22:20:00+00:00',
                         '2022-05-09 22:25:00+00:00'
                         ]
        cron = AWSCron(cron)
        dt = datetime.datetime(2020, 5, 9, 22, 30, 57, tzinfo=datetime.timezone.utc)
        results = []
        for expected in expected_list:
            print(f"Input {cron}, occurrence: {dt}")
            dt = cron.occurrence(dt).next()
            results.append(str(dt))
            print(f"Result: {dt}\tExpected: {expected}\n")
            self.assertEqual(expected, str(dt))


    def test_generate_multiple_next_8(self):
        """At 09:30 AM, between day L and 2 of the month
           cron(Minutes Hours Day-of-month Month Day-of-week Year)
           L ==>> This character is used to specify last day of the month or week
           - ==>> This character is used to specifies ranges.
        :return:
        """
        cron = '30 9 L-2 * ? *'
        expected_list = ['2020-05-29 09:30:00+00:00',
                         '2020-06-28 09:30:00+00:00',
                         '2020-07-29 09:30:00+00:00',
                         '2020-08-29 09:30:00+00:00',
                         '2020-09-28 09:30:00+00:00',
                         '2020-10-29 09:30:00+00:00',
                         '2020-11-28 09:30:00+00:00'
                         ]
        cron = AWSCron(cron)
        dt = datetime.datetime(2020, 5, 9, 22, 30, 57, tzinfo=datetime.timezone.utc)
        results = []
        for expected in expected_list:
            print(f"Input {cron}, occurrence: {dt}")
            dt = cron.occurrence(dt).next()
            results.append(str(dt))
            print(f"Result: {dt}\tExpected: {expected}\n")
            self.assertEqual(expected, str(dt))

    def test_generate_multiple_next_9(self):
        """ At 09:30 AM, on the weekday nearest day 3 of the month
            cron(Minutes Hours Day-of-month Month Day-of-week Year)
            W ==>>This character is used to specify the weekday (Monday-Friday) nearest the given day.
        :return:
        """
        cron = '30 9 3W * ? *'
        expected_list = ['2020-08-03 09:30:00+00:00',
                         '2020-09-03 09:30:00+00:00',
                         '2020-10-02 09:30:00+00:00'
                         ]

        cron = AWSCron(cron)
        dt = datetime.datetime(2020, 7, 31, 22, 30, 57, tzinfo=datetime.timezone.utc)
        results = []
        for expected in expected_list:
            print(f"Input {cron}, occurrence: {dt}")
            dt = cron.occurrence(dt).next()
            results.append(str(dt))
            print(f"Result: {dt}\tExpected: {expected}\n")
            self.assertEqual(expected, str(dt))


    def test_generate_multiple_next_10(self):
        """ At 09:30 AM, on the weekday nearest day 3 of the month
            cron(Minutes Hours Day-of-month Month Day-of-week Year)
            W ==>>This character is used to specify the weekday (Monday-Friday) nearest the given day.
        :return:
        """
        cron = '30 9 3W * ? *'
        expected_list = ['2020-05-04 09:30:00+00:00']

        cron = AWSCron(cron)
        dt = datetime.datetime(2020, 4, 30, 22, 30, 57, tzinfo=datetime.timezone.utc)
        results = []
        for expected in expected_list:
            print(f"Input {cron}, occurrence: {dt}")
            dt = cron.occurrence(dt).next()
            results.append(str(dt))
            print(f"Result: {dt}\tExpected: {expected}\n")
            self.assertEqual(expected, str(dt))

    def test_generate_multiple_next_11(self):
        """ At 09:30 AM, on the weekday nearest day 3 of the month
            cron(Minutes Hours Day-of-month Month Day-of-week Year)
            W ==>>This character is used to specify the weekday (Monday-Friday) nearest the given day.
        :return:
        """
        cron = '0 0 31W * ? 2020'
        expected_list = ['2020-05-29 00:00:00+00:00',
                         '2020-07-31 00:00:00+00:00',
                         '2020-08-31 00:00:00+00:00']

        cron = AWSCron(cron)
        dt = datetime.datetime(2020, 4, 30, 22, 30, 57, tzinfo=datetime.timezone.utc)
        results = []
        for expected in expected_list:
            print(f"Input {cron}, occurrence: {dt}")
            dt = cron.occurrence(dt).next()
            results.append(str(dt))
            print(f"Result: {dt}\tExpected: {expected}\n")
            self.assertEqual(expected, str(dt))


    def test_generate_multiple_next_12(self):
        """ At 09:30 AM, on the weekday nearest day 3 of the month
            cron(Minutes Hours Day-of-month Month Day-of-week Year)
            W ==>>This character is used to specify the weekday (Monday-Friday) nearest the given day.
        :return:
        """
        cron = '0 0 31W * ? *'
        expected_list = ['2020-12-31 00:00:00+00:00',
                         '2021-01-29 00:00:00+00:00',]

        cron = AWSCron(cron)
        dt = datetime.datetime(2020, 12, 30, 22, 30, 57, tzinfo=datetime.timezone.utc)
        results = []
        for expected in expected_list:
            print(f"Input {cron}, occurrence: {dt}")
            dt = cron.occurrence(dt).next()
            results.append(str(dt))
            print(f"Result: {dt}\tExpected: {expected}\n")
            self.assertEqual(expected, str(dt))

    def test_generate_multiple_next_12(self):
        """ On 4th and 5th minute of every hour for every day for every month and every year
            Testing if order in the minute affects results when using the wild card ","
            cron(Minutes Hours Day-of-month Month Day-of-week Year)
            W ==>>This character is used to specify the weekday (Monday-Friday) nearest the given day.
        :return:
        """
        cron = '5,4 * * * ? *'
        expected_list = ['2020-04-30 23:04:00+00:00',
                         '2020-04-30 23:05:00+00:00',
                         '2020-05-01 00:04:00+00:00',
                         '2020-05-01 00:05:00+00:00',
                         '2020-05-01 01:04:00+00:00',
                         '2020-05-01 01:05:00+00:00',
                         '2020-05-01 02:04:00+00:00',
                         '2020-05-01 02:05:00+00:00',
                         '2020-05-01 03:04:00+00:00',
                         '2020-05-01 03:05:00+00:00']

        cron = AWSCron(cron)
        dt = datetime.datetime(2020, 4, 30, 22, 30, 57, tzinfo=datetime.timezone.utc)
        results = []
        for expected in expected_list:
            print(f"Input {cron}, occurrence: {dt}")
            dt = cron.occurrence(dt).next()
            results.append(str(dt))
            print(f"Result: {dt}\tExpected: {expected}\n")
            self.assertEqual(expected, str(dt))




    def test_generate_multiple_next_occurences13(self):
        """At 12:15 PM, only on Sunday and Monday
           Testing if order in the Month or Day-of-week affects results when using the wild card ","
           cron(Minutes Hours Day-of-month Month Day-of-week Year)
        :return:
        """
        cron = '15 12 ? AUG,JUL mon,sun *'
        expected_list = ['2021-07-04 12:15:00+00:00',
                         '2021-07-05 12:15:00+00:00',
                         '2021-07-11 12:15:00+00:00',
                         '2021-07-12 12:15:00+00:00',
                         '2021-07-18 12:15:00+00:00',
                         '2021-07-19 12:15:00+00:00',
                         '2021-07-25 12:15:00+00:00',
                         '2021-07-26 12:15:00+00:00',
                         '2021-08-01 12:15:00+00:00',
                         '2021-08-02 12:15:00+00:00'
                         ]
        cron = AWSCron(cron)
        dt = datetime.datetime(2020, 12, 7, 15, 57, 37, tzinfo=datetime.timezone.utc)
        results = []
        # for x in range(10):
        #     dt = cron.occurrence(dt).next()
        #     print(f"Result: {dt}")
        for expected in expected_list:
            print(f"Input {cron}, occurrence: {dt}")
            dt = cron.occurrence(dt).next()
            results.append(str(dt))
            print(f"Result: {dt}\tExpected: {expected}\n")
            self.assertEqual(expected, str(dt))



    def test_generate_multiple_next_14(self):
        """Every minute between 10:00 PM and 10:/5 PM, on day 09 of the month, only in May,
           only in 2020, 2021, and 2022
           Testing if order in the Year affects results when using the wild card ","
           cron(Minutes Hours Day-of-month Month Day-of-week Year)
           / ==>> This character is used to specify increments.
           - ==>> This character is used to specifies ranges.
        :return:
        """
        cron = '0-29/5 22 09 05 ? 2021,2020,2022'
        expected_list = ['2021-05-09 22:00:00+00:00',
                         '2021-05-09 22:05:00+00:00',
                         '2021-05-09 22:10:00+00:00',
                         '2021-05-09 22:15:00+00:00',
                         '2021-05-09 22:20:00+00:00',
                         '2021-05-09 22:25:00+00:00',
                         '2022-05-09 22:00:00+00:00',
                         '2022-05-09 22:05:00+00:00',
                         '2022-05-09 22:10:00+00:00',
                         '2022-05-09 22:15:00+00:00',
                         '2022-05-09 22:20:00+00:00',
                         '2022-05-09 22:25:00+00:00'
                         ]
        cron = AWSCron(cron)
        dt = datetime.datetime(2020, 5, 9, 22, 30, 57, tzinfo=datetime.timezone.utc)
        results = []
        for expected in expected_list:
            print(f"Input {cron}, occurrence: {dt}")
            dt = cron.occurrence(dt).next()
            results.append(str(dt))
            print(f"Result: {dt}\tExpected: {expected}\n")
            self.assertEqual(expected, str(dt))

    def test_generate_multiple_next_occurences15(self):
        """
        Tests the generation of multiple next occurrences 
        from a specific CRON expression. Ensures that
        days_of_week are within the expected range.
        :return: None
        """
        cron = '00 4 ? * 3-1 *'
        expected_list= ['2024-11-14 04:00:00+00:00',
                        '2024-11-15 04:00:00+00:00',
                        '2024-11-16 04:00:00+00:00',
                        '2024-11-17 04:00:00+00:00',

                        '2024-11-19 04:00:00+00:00',
                        '2024-11-20 04:00:00+00:00',
                        '2024-11-21 04:00:00+00:00',
                        '2024-11-22 04:00:00+00:00',
                        '2024-11-23 04:00:00+00:00',
                        '2024-11-24 04:00:00+00:00']
        cron = AWSCron(cron)
        dt = datetime.datetime(2024, 11, 13, 12, 30, 57, tzinfo=datetime.timezone.utc)
        results = []
        for expected in expected_list:
            print(f"Input {cron}, occurrence: {dt}")
            dt = cron.occurrence(dt).next()
            results.append(str(dt))
            print(f"Result: {dt}\tExpected: {expected}\n")
            self.assertEqual(expected, str(dt))


if __name__ == '__main__':
    unittest.main()
