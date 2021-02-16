
# -*- coding: utf-8 -*-

import unittest
import datetime
from datetime import timezone
from pyawscron.awscron import AWSCron

class NextTestCase(unittest.TestCase):


    def setUp(self):
        pass


    def tearDown(self):
        pass
    def test_nest1(self):
        """
        should generate multiple next occurences #1

        """

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
        print(cron)
        dt = datetime.datetime(2020, 5, 9, 22, 30, 57, tzinfo=datetime.timezone.utc)
        results = []
        for expected in expected_list:
            dt = cron.occurance(dt).next()
            results.append(str(dt))
        print(expected_list)
        self.assertListEqual(expected_list, results)
        # for x in range(1,11,1):
        #     print(f"Test{x}")
        #     print(f"In: {str(dt)}")
        #     dt = cron.occurance(dt).next()
        #     print(f"Out: {str(dt)}")
        #     print("")

        #     results.append(str(dt))
        # self.assertEqual(expected, results)
