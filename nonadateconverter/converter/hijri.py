from ..core import HijriAbstract
from hijridate import Hijri, Gregorian
from persiantools.jdatetime import JalaliDate
from typing import Tuple
from datetime import datetime, date


class HijriConverter(HijriAbstract):

    def __init__(
            self,
            year=None,
            month=None,
            day=None
    ) -> None:
        if not year or not month or not day:
            raise TypeError("missing 3 required positional arguments: 'year', 'month', and 'day'")
        super().__init__(year, month, day)

    def hijri_to_gregorian(self) -> Tuple:
        try:
            hijri_date = Hijri(self.year, self.month, self.day).to_gregorian()
            return hijri_date.year, hijri_date.month, hijri_date.day
        except ValueError:
            raise ValueError

    def hijri_to_jalali(self) -> Tuple:
        try:
            gregorian_date = self.hijri_to_gregorian()
            year, month, day = gregorian_date
            jalali_date = JalaliDate.to_jalali(year, month, day)
            return jalali_date.year, jalali_date.month, jalali_date.day
        except ValueError:
            raise ValueError

    def weekday(self) -> str:
        try:
            hijri_date = Hijri(self.year, self.month, self.day).to_gregorian()

            # Create a datetime object from the Gregorian date
            date_object = datetime(hijri_date.year, hijri_date.month, hijri_date.day)

            # Get the weekday of the date
            weekday = date_object.weekday()

            # Define a list of weekdays
            weekdays = ["Al Ithnayn", "Ath Thulatha", "Al Arbia", "Al khamis", "Al Jumuah", "As Sabt", "Al Ahad"]

            return weekdays[weekday]
        except ValueError:
            raise ValueError

    def elapsedtime(self) -> Tuple:
        try:
            date1 = datetime(self.year, self.month, self.day)
            now = Hijri(self.year, self.month, self.day).today()
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

    @classmethod
    def now(cls) -> Tuple:
        # Get today's date
        today = date.today()

        # Convert today's Gregorian date to Hijri
        hijri_today = Gregorian(today.year, today.month, today.day).to_hijri()
        return hijri_today.year, hijri_today.month, hijri_today.day
