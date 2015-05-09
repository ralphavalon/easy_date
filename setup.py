from distutils.core import setup
import easy_date

setup(
    # Application name:
    name="easy-date",

    # Version number (initial):
    version=easy_date.__version__,

    # Application author details:
    author="Raphael Amoedo",
    author_email="avalon.ralph@gmail.com",

    # Scripts
    py_modules=["easy_date", "date_converter"],
    scripts=["easy_date.py", "date_converter.py"],


    # Include additional files into the package
    #include_package_data=True,

    # Details
    url="http://pypi.python.org/pypi/easy-date/",

    #
    license="MIT",
    description="Easy and readable way to convert dates.",

)
