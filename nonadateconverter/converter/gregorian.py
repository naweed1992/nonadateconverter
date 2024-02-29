from ..core import GregorianAbstract
from ..utils import validate_args
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
        validate_args(self._year, self._month, self._day)

    def gregorian_to_hijri(self) -> Tuple:
        gregorian_date = Gregorian(self._year, self._month, self._day)
        hijri_date = gregorian_date.to_hijri()
        return hijri_date.year, hijri_date.month, hijri_date.day

    def gregorian_to_jalali(self):
        gregorian_date = jdatetime.date.fromgregorian(year=self._year, month=self._month, day=self._day)
        return gregorian_date.year, gregorian_date.month, gregorian_date.day

    @classmethod
    def now(cls) -> Tuple:
        now = datetime.now()
        return now.year, now.month, now.day

    def weekday(self) -> str:
        timezone_local = timezone(timedelta(hours=3, minutes=30))
        date = datetime.now(tz=timezone_local)
        weekday = date.strftime("%A")
        return weekday

    def elapsedtime(self) -> Tuple:
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
