from datetime import date, datetime
from converter import Converter

converter = Converter()

def convert_from_string(string, current_format, to_format, to_type=str):
    if to_type == str:
        return converter.string_to_string(string, current_format, to_format)
    elif to_type == datetime:
        return converter.string_to_datetime(string, current_format, to_format)
    elif to_type == date:
        return converter.string_to_date(string, current_format)

def convert_from_datetime(from_datetime, to_format, to_type=str):
    if to_type == str:
        return converter.datetime_to_string(from_datetime, to_format)
    elif to_type == datetime:
        return converter.datetime_to_datetime(from_datetime, to_format)
    elif to_type == date:
        return converter.datetime_to_date(from_datetime)

def convert_from_date(from_date, to_format, to_type=str):
    if to_type == str:
        return converter.date_to_string(from_date, to_format)
    elif to_type == datetime:
        return converter.date_to_datetime(from_date)