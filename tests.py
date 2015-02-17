from csv import excel

__author__ = 'ralphavalon' #Ralph Avalon

import unittest
from converter import Converter
from datetime import datetime, date

class ConverterTest(unittest.TestCase):

    converter = None
    expected_minutes = expected_day = 15
    expected_hour = expected_month = 02
    expected_year = 2015
    test_date = date(expected_year, expected_month, expected_day)
    test_date_string = '%d/%02d/%d' % (expected_day, expected_month, expected_year)
    test_datetime = datetime(expected_year, expected_month, expected_day, expected_hour, expected_minutes)
    expected_format = '%d-%d-%02d' % (expected_year, expected_day, expected_month)


    def setUp(self):
        self.converter = Converter()

    def test_string_to_date(self):
        result = self.converter.string_to_date(self.test_date_string, '%d/%m/%Y')
        self.assertEquals(date, type(result))
        self.assertEquals(self.expected_year, result.year)
        self.assertEquals(self.expected_month, result.month)
        self.assertEquals(self.expected_day, result.day)

    def test_string_to_datetime(self):
        result = self.converter.string_to_datetime(self.test_date_string, '%d/%m/%Y', '%Y-%d-%m')
        self.assertEquals(datetime, type(result))
#        self.assertIn(self.expected_format, str(result))
        self.assertEquals(self.expected_year, result.year)
        self.assertEquals(self.expected_month, result.month)
        self.assertEquals(self.expected_day, result.day)

    def test_string_to_string(self):
        result = self.converter.string_to_string(self.test_date_string, '%d/%m/%Y', '%Y-%d-%m')
        self.assertEquals(str, type(result))
        self.assertEquals(self.expected_format, str(result))

    def test_date_to_string(self):
        result = self.converter.date_to_string(self.test_date, '%Y-%d-%m')
        self.assertEquals(str, type(result))
        self.assertEquals(self.expected_format, str(result))

    def test_date_to_datetime(self):
        result = self.converter.date_to_datetime(self.test_date)
        self.assertEquals(datetime, type(result))
        self.assertEquals(self.expected_year, result.year)
        self.assertEquals(self.expected_month, result.month)
        self.assertEquals(self.expected_day, result.day)

    def test_datetime_to_date(self):
        result = self.converter.datetime_to_date(self.test_datetime)
        self.assertEquals(date, type(result))
        self.assertEquals(self.expected_year, result.year)
        self.assertEquals(self.expected_month, result.month)
        self.assertEquals(self.expected_day, result.day)

    def test_datetime_to_datetime(self):
        result = self.converter.datetime_to_datetime(self.test_datetime, '%d/%m/%Y')
        self.assertEquals(datetime, type(result))
        self.assertEquals(self.expected_year, result.year)
        self.assertEquals(self.expected_month, result.month)
        self.assertEquals(self.expected_day, result.day)
        self.assertEquals(0, result.hour)
        self.assertEquals(0, result.minute)

if __name__ == '__main__':
    unittest.main(verbosity=2)