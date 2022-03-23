# MIT License

# Copyright (c) 2022 [FacuFalcone]

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

from datetime import datetime as dt
import pytz

def get_timezone(country: str) -> str:
    """
    Get the timezone of a country.
    """
    return pytz.timezone(country)

def get_country_name(tz: str) -> str:
    """
    Get the name of a country.
    """
    return tz.split('/')[-1]

def get_date(tz):
    """
    Get the date in the timezone.
    """
    return dt.now(tz)

def print_time_zones(countries: set) -> None:
    """
    Print the timezones of the countries.
    """
    for country in countries:
        count_name = get_country_name(country)
        country_tz = get_timezone(country)
        country_date = dt.now(country_tz)
        print(f'The current time in {count_name} is {country_tz.localize(dt.now())}')
        print(f'The current date in {count_name} is {country_date.strftime("%A, %B %d of %Y %H:%M:%S")}')
        print(f'The current date in {count_name} is {country_date.strftime("%d-%m-%Y %I:%M:%S %p")}\n')
        
if __name__ == '__main__':
    COUNTRIES_SETS = {'America/Argentina/Buenos_Aires', 'America/Bogota'}
    print_time_zones(COUNTRIES_SETS)

