#!/usr/bin/env python
"""
Easy_date is a simple converter that manipulates date, datetime, timestamp and str dates. It has no dependencies other than the
Python Standard Library.

Copyright (c) 2015, Raphael Amoedo.
License: MIT (see LICENSE.md for details)
"""

__author__ = 'Raphael Amoedo' #a.k.a. Ralph Avalon
__version__ = '0.1.3'
__license__ = 'MIT'

from datetime import date, datetime
import date_converter as converter

def convert_from_string(string, current_format, to_format, to_type=str):
    if to_type == str:
        return converter.string_to_string(string, current_format, to_format)
    elif to_type == datetime:
        return converter.string_to_datetime(string, current_format, to_format)
    elif to_type == date:
        return converter.string_to_date(string, current_format)
    elif to_type == float:
        return converter.string_to_timestamp(string, current_format)

def convert_from_datetime(from_datetime, to_format, to_type=str):
    if to_type == str:
        return converter.datetime_to_string(from_datetime, to_format)
    elif to_type == datetime:
        return converter.datetime_to_datetime(from_datetime, to_format)
    elif to_type == date:
        return converter.datetime_to_date(from_datetime)
    elif to_type == float:
        return converter.datetime_to_timestamp(from_datetime)

def convert_from_date(from_date, to_format, to_type=str):
    if to_type == str:
        return converter.date_to_string(from_date, to_format)
    elif to_type == datetime:
        return converter.date_to_datetime(from_date)
    elif to_type == float:
        return converter.date_to_timestamp(from_date)

def convert_from_timestamp(timestamp, to_format, to_type=str):
    if to_type == str:
        return converter.timestamp_to_string(timestamp, to_format)
    elif to_type == datetime:
        return converter.timestamp_to_datetime(timestamp, to_format)
    elif to_type == date:
        return converter.timestamp_to_date(timestamp)
