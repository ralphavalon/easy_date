# README #

Let's face it: there's no JodaTime for Python, and dealing with date, datetime, timestamp in Python it's not very readable or easy to understand. Easy_date can convert between str, date, datetime and timestamp easily for you and it is readable.

### Installation ###

Install the latest stable release with:

``pip install easy_date``

or 

``easy_install -U easy_date``

There are no hard dependencies other than the Python standard library.


### How do I convert dates? ###

#### Can use two ways:
    
* Using **easy_date**

```
#!python
from datetime import date, datetime
import easy_date

str_date = '25/12/2014' #%d/%m/%Y

#convert_from_string(string, current_format, to_format, to_type)
new_str_date = easy_date.convert_from_string(str_date, '%d/%m/%Y', '%m-%d-%Y') # str is default return type
date_time = easy_date.convert_from_string(str_date, '%d/%m/%Y', '%Y-%m-%d', datetime)
timestamp = easy_date.convert_from_string(str_date, '%d/%m/%Y', None, float)
my_date = easy_date.convert_from_string(str_date, '%d/%m/%Y', None, date)

```

   
* Using **date_converter**

```
#!python
from datetime import date, datetime
from date_converter import Date_Converter

date_converter = Date_Converter()
str_date = '25/12/2014' #%d/%m/%Y

#string_to_string(string, current_format, to_format)
new_str_date = date_converter.string_to_string(str_date, '%d/%m/%Y', '%m-%d-%Y')
#string_to_datetime(string, current_format, to_format)
date_time = date_converter.string_to_datetime(str_date, '%d/%m/%Y', '%Y-%m-%d')
#string_to_timestamp(string, current_format)
timestamp = date_converter.string_to_timestamp(str_date, '%d/%m/%Y')
#string_to_date(string, current_format)
my_date = date_converter.string_to_date(str_date, '%d/%m/%Y')

```

### Available methods ###

* from **easy_date**


```
#!python

#Acceptable types: (str, datetime.datetime, datetime.date, float)
convert_from_string(string, current_format, to_format, to_type=str)

#Acceptable types: (str, datetime.datetime, datetime.date, float)
convert_from_datetime(from_datetime, to_format, to_type=str)

#Acceptable types: (str, datetime.datetime, float)
convert_from_date(from_date, to_format, to_type=str)

#Acceptable types: (str, datetime.datetime, datetime.date)
convert_from_timestamp(timestamp, to_format, to_type=str)

```


* from **date_converter**

```
#!python

#from datetime.date
date_to_datetime(from_date)
date_to_string(from_date, to_format)
date_to_timestamp(from_date)

#from datetime.datetime
datetime_to_date(from_datetime)
datetime_to_datetime(from_datetime, to_format)
datetime_to_string(from_datetime, to_format)
datetime_to_timestamp(from_datetime)

#from str
string_to_date(string, current_format)
string_to_datetime(string, current_format, to_format)
string_to_string(string, current_format, to_format)
string_to_timestamp(string, current_format)

#from float
timestamp_to_date(timestamp)
timestamp_to_datetime(timestamp, to_format)
timestamp_to_string(timestamp, to_format)

```

### Contribution guidelines ###

* Every help or suggestion is welcome.

### License ###

* Code and documentation are available according to the MIT License (see LICENSE.md).