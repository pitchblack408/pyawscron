
# -*- coding: utf-8 -*-

import unittest
import datetime
from src.pyawscron import AWSCron

class PrevTestCase(unittest.TestCase):


    def setUp(self):
        print(self._testMethodName)


    def tearDown(self):
        pass

    def test_generate_multiple_prev_occurences1(self):
        """At 23, 24, and 25 minutes past the hour, at 05:00 PM and 06:00 PM,
           on day 25 of the month, every 4 months, March through December,
           only in 2019, 2020, 2021, 2023, and 2028
           cron(Minutes Hours Day-of-month Month Day-of-week Year)
           / ==>> This character is used to specify increments.
        :return:
        """
        cron = '23,24,25 17,18 25 MAR/4 ? 2019,2020,2021,2023,2028'

        expected_list= ['2020-03-25 18:25:00+00:00',
                        '2020-03-25 18:24:00+00:00',
                        '2020-03-25 18:23:00+00:00',
                        '2020-03-25 17:25:00+00:00',
                        '2020-03-25 17:24:00+00:00',
                        '2020-03-25 17:23:00+00:00',
                        '2019-11-25 18:25:00+00:00',
                        '2019-11-25 18:24:00+00:00',
                        '2019-11-25 18:23:00+00:00',
                        '2019-11-25 17:25:00+00:00'
                        ]
        cron = AWSCron(cron)
        dt = datetime.datetime(2020, 5, 9, 22, 30, 57, tzinfo=datetime.timezone.utc)
        results = []
        for expected in expected_list:
            print(f"Input {cron}, occurrence: {dt}")
            dt = cron.occurrence(dt).prev()
            results.append(str(dt))
            print(f"Result: {dt}\tExpected: {expected}\n")
            self.assertEqual(expected, str(dt))

if __name__ == '__main__':
    unittest.main()