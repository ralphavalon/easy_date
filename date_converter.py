#!/usr/bin/env python
"""
Easy_date is a simple converter that manipulates date, datetime, timestamp and str dates. It has no dependencies other than the
Python Standard Library.

Copyright (c) 2015, Raphael Amoedo.
License: MIT (see LICENSE.md for details)
"""

__author__ = 'Raphael Amoedo' #a.k.a. Ralph Avalon
__license__ = 'MIT'

from datetime import datetime
import time

date_default_format = '%Y-%m-%d'

def date_to_datetime(from_date):
    return datetime(from_date.year, from_date.month, from_date.day)

def date_to_string(from_date, to_format):
    return datetime(from_date.year, from_date.month, from_date.day).strftime(to_format)

def date_to_timestamp(from_date):
    return time.mktime(from_date.timetuple())

def datetime_to_date(from_datetime):
    return from_datetime.date()

def datetime_to_datetime(from_datetime, to_format):
    return datetime.strptime(from_datetime.strftime(to_format), to_format)

def datetime_to_string(from_datetime, to_format):
    return from_datetime.strftime(to_format)

def datetime_to_timestamp(from_datetime):
    return time.mktime(from_datetime.timetuple())

def string_to_date(string, current_format):
    return datetime.strptime(string, current_format).date()

def string_to_datetime(string, current_format, to_format=None):
    if to_format:
        return datetime.strptime(datetime.strptime(string, current_format).strftime(to_format), to_format)
    return datetime.strptime(string, current_format)

def string_to_string(string, current_format, to_format):
    return datetime.strptime(string, current_format).strftime(to_format)

def string_to_timestamp(string, current_format):
    return time.mktime(datetime.strptime(string, current_format).timetuple())

def timestamp_to_date(timestamp):
    return datetime.fromtimestamp(timestamp).date()

def timestamp_to_datetime(timestamp, to_format=None):
    if to_format:
        return datetime.strptime(datetime.fromtimestamp(timestamp).strftime(to_format), to_format)
    return datetime.fromtimestamp(timestamp)

def timestamp_to_string(timestamp, to_format):
    return datetime.fromtimestamp(timestamp).strftime(to_format)
