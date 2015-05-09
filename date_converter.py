#!/usr/bin/env python
"""
Easy_date is a simple converter that manipulates date, datetime, timestamp and str dates. It has no dependencies other than the
Python Standard Library.

Copyright (c) 2015, Raphael Amoedo.
License: MIT (see LICENSE.md for details)
"""

__author__ = 'Raphael Amoedo'
__license__ = 'MIT'

from datetime import datetime
import time

class Date_Converter:

    date_default_format = '%Y-%m-%d'

    def date_to_datetime(self, from_date):
        return datetime(from_date.year, from_date.month, from_date.day)

    def date_to_string(self, from_date, to_format):
        return datetime(from_date.year, from_date.month, from_date.day).strftime(to_format)

    def date_to_timestamp(self, from_date):
        return time.mktime(from_date.timetuple())

    def datetime_to_date(self, from_datetime):
        return from_datetime.date()

    def datetime_to_datetime(self, from_datetime, to_format):
        return datetime.strptime(from_datetime.strftime(to_format), to_format)

    def datetime_to_string(self, from_datetime, to_format):
        return from_datetime.strftime(to_format)

    def datetime_to_timestamp(self, from_datetime):
        return time.mktime(from_datetime.timetuple())

    def string_to_date(self, string, current_format):
        return datetime.strptime(string, current_format).date()

    def string_to_datetime(self, string, current_format, to_format):
        return datetime.strptime(datetime.strptime(string, current_format).strftime(to_format), to_format)

    def string_to_string(self, string, current_format, to_format):
        return datetime.strptime(string, current_format).strftime(to_format)

    def string_to_timestamp(self, string, current_format):
        return time.mktime(datetime.strptime(string, current_format).timetuple())

    def timestamp_to_date(self, timestamp):
        return datetime.fromtimestamp(timestamp).date()

    def timestamp_to_datetime(self, timestamp, to_format):
        return datetime.strptime(datetime.fromtimestamp(timestamp).strftime(to_format), to_format)

    def timestamp_to_string(self, timestamp, to_format):
        return datetime.fromtimestamp(timestamp).strftime(to_format)