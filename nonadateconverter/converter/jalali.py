from ..core import JalaliAbstract
from persiantools.jdatetime import JalaliDate, JalaliDateTime
from hijridate import Gregorian
from typing import Tuple
import pytz
from datetime import date


class JalaliConverter(JalaliAbstract):

    def __init__(
            self,
            year=None,
            month=None,
            day=None
    ) -> None:
        if year is None and month is None and day is None:
            now = JalaliDate.today()
            self._year = now.year
            self._month = now.month
            self._day = now.day
        else:
            self._year = year
            self._month = month
            self._day = day
        try:
            self._year = int(self._year)
            self._month = int(self._month)
            self._day = int(self._day)
        except ValueError:
            raise ValueError('Invalid year, month, day type, allowed types are integer and string')

    def jalali_to_hijri(self) -> Tuple:
        try:
            year, month, day = self.jalali_to_gregorian()
            gregorian_date = Gregorian(year, month, day)
            hijri_date = gregorian_date.to_hijri()
            return hijri_date.year, hijri_date.month, hijri_date.day
        except ValueError:
            raise ValueError

    def jalali_to_gregorian(self) -> Tuple:
        try:
            time = JalaliDate(self._year, self._month, self._day).to_gregorian()
            return time.year, time.month, time.day
        except ValueError:
            raise ValueError

    @classmethod
    def now(cls) -> Tuple:
        now = JalaliDate.today()
        return now.year, now.month, now.day

    def weekday(self) -> str:
        try:
            time = JalaliDateTime(self._year, self._month, self._day, tzinfo=pytz.utc).strftime("%c")
            return time.split(' ')[0]
        except ValueError:
            raise ValueError

    def elapsedtime(self) -> Tuple:
        try:
            date1 = JalaliDate(self._year, self._month, self._day).to_gregorian()
            now = JalaliDate(self._year, self._month, self._day).today().to_gregorian()
            date2 = date(now.year, now.month, now.day)
            delta = date2 - date1
            days = delta.days

            # Calculate the difference in years and months
            years = days // 365
            months = (days % 365) // 30  # Approximation: assumes a month is  30 days

            # Calculate the remaining days after accounting for years and months
            remaining_days = (days % 365) % 30

            return years, months, remaining_days
        except ValueError:
            raise ValueError
