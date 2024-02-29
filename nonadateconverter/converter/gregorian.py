from ..core import GregorianAbstract
from hijridate import Gregorian
import jdatetime
from typing import Tuple
from datetime import datetime, timezone, timedelta


class GregorianConverter(GregorianAbstract):
    def __init__(
            self,
            year=None,
            month=None,
            day=None
    ) -> None:
        if year is None and month is None and day is None:
            now = datetime.now()
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

    def gregorian_to_hijri(self) -> Tuple:
        try:
            gregorian_date = Gregorian(self._year, self._month, self._day)
            hijri_date = gregorian_date.to_hijri()
            return hijri_date.year, hijri_date.month, hijri_date.day
        except ValueError:
            raise ValueError

    def gregorian_to_jalali(self):
        try:
            gregorian_date = jdatetime.date.fromgregorian(year=self._year, month=self._month, day=self._day)
            return gregorian_date.year, gregorian_date.month, gregorian_date.day
        except ValueError:
            raise ValueError

    @classmethod
    def now(cls) -> Tuple:
        now = datetime.now()
        return now.year, now.month, now.day

    def weekday(self) -> str:
        try:
            timezone_local = timezone(timedelta(hours=3, minutes=30))
            date = datetime.now(tz=timezone_local)
            weekday = date.strftime("%A")
            return weekday
        except ValueError:
            raise ValueError

    def elapsedtime(self) -> Tuple:
        try:
            date1 = datetime(self._year, self._month, self._day)
            now = datetime.now()
            date2 = datetime(now.year, now.month, now.day)
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
