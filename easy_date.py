from datetime import date, datetime

date_default_format = '%Y-%m-%d'

def convert_from_string(string, current_format, to_format, to_type=str):
    formatted_string = datetime.strptime(string, current_format).strftime(to_format)
    if to_type == str:
        return formatted_string
    elif to_type == datetime:
        return datetime.strptime(formatted_string, to_format)
    elif to_type == date:
        return datetime.strptime(formatted_string, to_format).date()

def convert_from_datetime(from_datetime, to_format, to_type=str):
    formatted_datetime = from_datetime.strftime(to_format)
    if to_type == str:
        return formatted_datetime
    elif to_type == datetime:
        return datetime.strptime(formatted_datetime, to_format)
    elif to_type == date:
        return datetime.strptime(formatted_datetime, to_format).date()

def convert_from_date(from_date, to_format, to_type=str):
    formatted_date = datetime.strptime(str(from_date), date_default_format).strftime(to_format)
    if to_type == str:
        return formatted_date
    elif to_type == datetime:
        return datetime(from_date.year, from_date.month, from_date.day)
    elif to_type == date:
        return datetime.strptime(formatted_date, to_format).date()
#print convert_from_string('20/02/2012', '%d/%m/%Y', '%d-%m', date)
#print convert_from_datetime(convert_from_string('20/02/2012', '%d/%m/%Y', '%d-%m', datetime),'%m-%d', datetime)