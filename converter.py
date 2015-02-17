from datetime import date, datetime

class Converter:

    date_default_format = '%Y-%m-%d'

    def date_to_datetime(self, from_date):
        return datetime(from_date.year, from_date.month, from_date.day)

    def date_to_string(self, from_date, to_format):
        return datetime(from_date.year, from_date.month, from_date.day).strftime(to_format)

    def datetime_to_date(self, from_datetime):
        return from_datetime.date()

    def datetime_to_datetime(self, from_datetime, to_format):
        return datetime.strptime(from_datetime.strftime(to_format), to_format)

    def datetime_to_string(self, from_datetime, to_format):
        return from_datetime.strftime(to_format)

    def string_to_date(self, string, current_format):
        return datetime.strptime(string, current_format).date()

    def string_to_datetime(self, string, current_format, to_format):
        return datetime.strptime(datetime.strptime(string, current_format).strftime(to_format), to_format)

    def string_to_string(self, string, current_format, to_format):
        return datetime.strptime(string, current_format).strftime(to_format)