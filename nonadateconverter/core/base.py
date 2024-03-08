from abc import ABC, abstractmethod
from typing import Union


class Abstract(ABC):

    def __init__(
            self,
            year: Union[int, str],
            month: Union[int, str],
            day: Union[int, str]
    ):
        try:
            self.year = int(year)
            self.month = int(month)
            self.day = int(day)
        except ValueError:
            raise ValueError('allowed data is numeric')

    @classmethod
    @abstractmethod
    def now(cls):
        ...

    @abstractmethod
    def weekday(self):
        ...

    @abstractmethod
    def elapsedtime(self):
        ...


class HijriAbstract(Abstract):

    def __init__(self, year, month, day):
        super().__init__(year, month, day)

    @abstractmethod
    def hijri_to_gregorian(self):
        pass

    @abstractmethod
    def hijri_to_jalali(self):
        pass


class GregorianAbstract(Abstract):

    def __init__(self, year, month, day):
        super().__init__(year, month, day)

    @abstractmethod
    def gregorian_to_hijri(self):
        pass

    @abstractmethod
    def gregorian_to_jalali(self):
        pass


class JalaliAbstract(Abstract):

    def __init__(self, year, month, day):
        super().__init__(year, month, day)

    @abstractmethod
    def jalali_to_hijri(self):
        pass

    @abstractmethod
    def jalali_to_gregorian(self):
        pass
