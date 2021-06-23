
# -*- coding: utf-8 -*-

import unittest
from pyawscron.awscron import AWSCron


class ParseCronTestCase(unittest.TestCase):

    def setUp(self):
        print(self._testMethodName)

    def tearDown(self):
        print()

    def print_cron_results(self, cron_str, cron_obj):
        print(f"Input: {cron_str}")
        print("Result:")
        print(f"\t{cron_obj}")
        print(f"\tcron.minutes: {cron_obj.minutes}")
        print(f"\tcron.hours: {cron_obj.hours}")
        print(f"\tcron.days_of_month: {cron_obj.days_of_month}")
        print(f"\tcron.months: {cron_obj.months}")
        print(f"\tcron.days_of_week: {cron_obj.days_of_week}")
        print(f"\tcron.years: {cron_obj.years}")

    def test_cron_expressions1(self):
        """
        should parse AWS cron expressions #1
        """
        expected = {"minutes": [6], "hours": [4, 7, 10, 13, 16, 19, 22],
                    "daysOfMonth": [8, 18, 19, 20, 26, 27, 28], "months": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
                    "daysOfWeek": [], "years": [2020, 2021, 2022, 2023, 2024, 2025, 2026, 2027, 2028, 2029, 2030]}
        cron_str = '6 4/3 8,18-20,26-28 * ? 2020-2030'
        cron_obj = AWSCron(cron_str)
        self.print_cron_results(cron_str, cron_obj)
        self.assertEqual(expected["minutes"], cron_obj.minutes)
        self.assertEqual(expected["hours"], cron_obj.hours)
        self.assertEqual(expected["daysOfMonth"], cron_obj.days_of_month)
        self.assertEqual(expected["months"], cron_obj.months)
        self.assertEqual(expected["daysOfWeek"], cron_obj.days_of_week)
        self.assertEqual(expected["years"], cron_obj.years)


    def test_cron_expressions2(self):
        """
        should parse AWS cron expressions #2
        """
        expected = {"minutes": [15],
                    "hours": [10],
                    "daysOfMonth": [],
                    "months": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
                    "daysOfWeek": ['L',  6],
                    "years": [x for x in range(2002, 2025 + 1)]}
        cron_str = '15 10 ? * 6L 2002-2025'
        cron_obj = AWSCron(cron_str)
        self.print_cron_results(cron_str, cron_obj)
        self.assertEqual(expected["minutes"], cron_obj.minutes)
        self.assertEqual(expected["hours"], cron_obj.hours)
        self.assertEqual(expected["daysOfMonth"], cron_obj.days_of_month)
        self.assertEqual(expected["months"], cron_obj.months)
        self.assertEqual(expected["daysOfWeek"], cron_obj.days_of_week)
        self.assertEqual(expected["years"], cron_obj.years)


    def test_cron_expressions3(self):
        """
        should parse AWS cron expressions #3
        """
        expected = {"minutes": [0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55],
                    "hours": [10],
                    "daysOfMonth": [],
                    "months": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
                    "daysOfWeek": [2, 3, 4, 5, 6],
                    "years": [x for x in range(1970,  2199 + 1)]}

        cron_str = '*/5 10 ? * MON-FRI *'
        cron_obj = AWSCron(cron_str)
        self.print_cron_results(cron_str, cron_obj)
        self.assertEqual(expected["minutes"], cron_obj.minutes)
        self.assertEqual(expected["hours"], cron_obj.hours)
        self.assertEqual(expected["daysOfMonth"], cron_obj.days_of_month)
        self.assertEqual(expected["months"], cron_obj.months)
        self.assertEqual(expected["daysOfWeek"], cron_obj.days_of_week)
        self.assertEqual(expected["years"], cron_obj.years)


    def test_cron_expressions4(self):
        """
        should parse AWS cron expressions #4
        """
        expected = {"minutes": [0], "hours": [0, 3, 6, 9, 12, 15, 18, 21],
                    "daysOfMonth": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23,
                                    24, 25, 26, 27, 28, 29, 30, 31],
                    "months": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
                    "daysOfWeek": [],
                    "years": [x for x in range(1970,  2199 + 1)]}

        cron_str = '0 */3 */1 * ? *'
        cron_obj = AWSCron(cron_str)
        self.print_cron_results(cron_str, cron_obj)
        self.assertEqual(expected["minutes"], cron_obj.minutes)
        self.assertEqual(expected["hours"], cron_obj.hours)
        self.assertEqual(expected["daysOfMonth"], cron_obj.days_of_month)
        self.assertEqual(expected["months"], cron_obj.months)
        self.assertEqual(expected["daysOfWeek"], cron_obj.days_of_week)
        self.assertEqual(expected["years"], cron_obj.years)


    def test_cron_expressions5(self):
        """
        should parse AWS cron expressions #5
        """
        expected = {"minutes": [15],
                    "hours": [12],
                    "daysOfMonth": [],
                    "months": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
                    "daysOfWeek": [1, 2],
                    "years": [x for x in range(1970, 2199 + 1)]}

        cron_str = '15 12 ? * sun,mon *'
        cron_obj = AWSCron(cron_str)
        self.print_cron_results(cron_str, cron_obj)
        self.assertEqual(expected["minutes"], cron_obj.minutes)
        self.assertEqual(expected["hours"], cron_obj.hours)
        self.assertEqual(expected["daysOfMonth"], cron_obj.days_of_month)
        self.assertEqual(expected["months"], cron_obj.months)
        self.assertEqual(expected["daysOfWeek"], cron_obj.days_of_week)
        self.assertEqual(expected["years"], cron_obj.years)


    def test_cron_expressions6(self):
        """
        should parse AWS cron expressions #6
        """
        expected = {"minutes": [10],
                    "hours": [7, 12, 17, 22],
                    "daysOfMonth": [7],
                    "months": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
                    "daysOfWeek": [],
                    "years": [2020]}

        cron_str = '10 7/5 7 * ? 2020'
        cron_obj = AWSCron(cron_str)
        self.print_cron_results(cron_str, cron_obj)
        self.assertEqual(expected["minutes"], cron_obj.minutes)
        self.assertEqual(expected["hours"], cron_obj.hours)
        self.assertEqual(expected["daysOfMonth"], cron_obj.days_of_month)
        self.assertEqual(expected["months"], cron_obj.months)
        self.assertEqual(expected["daysOfWeek"], cron_obj.days_of_week)
        self.assertEqual(expected["years"], cron_obj.years)


    def test_cron_expressions7(self):
        """
        should parse AWS cron expressions #7
        """
        expected = {"minutes": [0, 5, 10, 15, 20, 25],
                    "hours": [22],
                    "daysOfMonth": [9],
                    "months": [5],
                    "daysOfWeek": [],
                    "years": [2020,2021,2022]}

        cron_str = '0-29/5 22 09 05 ? 2020,2021,2022'
        cron_obj = AWSCron(cron_str)
        self.print_cron_results(cron_str, cron_obj)
        self.assertEqual(expected["minutes"], cron_obj.minutes)
        self.assertEqual(expected["hours"], cron_obj.hours)
        self.assertEqual(expected["daysOfMonth"], cron_obj.days_of_month)
        self.assertEqual(expected["months"], cron_obj.months)
        self.assertEqual(expected["daysOfWeek"], cron_obj.days_of_week)
        self.assertEqual(expected["years"], cron_obj.years)





if __name__ == '__main__':
    unittest.main()
