from distutils.core import setup
import easy_date

setup(
    # Application name:
    name="easy_date",

    # Version number (initial):
    version=easy_date.__version__,

    # Application author details:
    author="Raphael Amoedo",
    author_email="avalon.ralph@gmail.com",

    # Scripts
    scripts=["easy_date.py", "date_converter.py"],


    # Include additional files into the package
    #include_package_data=True,

    # Details
    url="http://pypi.python.org/pypi/easy_date/",

    #
    license="LICENSE.md",
    description="Easy and readable way to convert dates.",

)