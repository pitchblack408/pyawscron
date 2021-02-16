
# -*- coding: utf-8 -*-

import unittest
import datetime
from datetime import timezone
from pyawscron.awscron import AWSCron

class NextTestCase(unittest.TestCase):


    def setUp(self):
        print(self._testMethodName)


    def tearDown(self):
        pass

    def test_generate_multiple_next_occurences1(self):
        cron = '23,24,25 17,18 25 MAR/4 ? 2020,2021,2023,2028'
        expected_list= [ '2020-07-25 17:23:00+00:00',
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
            print(f"Result: {dt}\n")
        self.assertListEqual(expected_list, results)


    def test_generate_multiple_next_occurences2(self):
        """

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
            print(f"Result: {dt}\n")
        self.assertListEqual(expected_list, results)